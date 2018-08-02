from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import csv, json, os
import apps.plot.plot as ploter
import apps.plot.functions as functions
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.core.files import File
from .forms import FileForm
from .models import UserFile
from io import StringIO
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# @login_required(redirect_field_name='login')
# def index(request):
# 	if request.method == 'POST':
# 		filepath = request.FILES.get('csv_file', False)
# 		if filepath:
# 			csv_file = request.FILES["csv_file"]
# 			if not csv_file.name.endswith('.csv'):
# 				messages.error(request,'El archivo no tiene extensión CSV')
# 				return redirect(reverse("upload_file"))
# 			#if file is too large, return
# 			if csv_file.multiple_chunks():
# 				messages.error(request,"El archivo es muy grande (%.2f MB)." % (csv_file.size/(1000*1000),))
# 				return redirect(reverse("upload_file"))		
# 			file_data = csv_file.read().decode("utf-8")
# 			plt = ploter.Plot(StringIO(file_data))
# 			request.session['data_plot'] = json.dumps(functions.FillJson(plt))
# 			return redirect('plot/')
# 		else:
# 			messages.error(request,'No ha seleccionado ningun archivo')
# 			return redirect(reverse("upload_file"))
# 	return render(request, 'plot/index.html')

@login_required(redirect_field_name='login')
def plot(request):	
	data_plot = request.session['data_plot']
	return render(request, 'plot/plot.html',{"data":data_plot, "user":request.user})

@login_required(redirect_field_name='login')
def interactions(request):
	html = '<img class="img-responsive" id="plot_img" src="../media/plot/'+str(request.user)+'users_interaction.png" />'
	return HttpResponse(html)

@login_required(login_url='accounts/login/')
def interv(request):
	html = '<img class="img-responsive" id="plot_img" src="../media/plot/'+str(request.user)+'users_speak.png" />'
	return HttpResponse(html)

@login_required(redirect_field_name='login')
def bar_graph(request):
	html = '<div id="graph" class="graph"></div>'
	data_plot = request.session['data_plot']
	return HttpResponse(json.dumps({
		"data": data_plot,
		"html": html
		}),
		content_type="aplication/json"
	)

@login_required(redirect_field_name='login')
def line_graph(request):
	html = '<div id="line" class="graph"></div>'
	return HttpResponse(json.dumps({
		"data": data_plot,
		"html": html
		}),
		content_type="aplication/json"
	)

@login_required(redirect_field_name='login')
def donut_graph(request):
	html = '<div id="donut" class="graph"></div>'
	data_plot = request.session['data_plot']
	return HttpResponse(json.dumps({
		"data": data_plot,
		"html": html
		}),
		content_type="aplication/json"
	)

@login_required(redirect_field_name='login')
def flare_json(request, user):
	if user == str(request.user):
		data_plot = request.session['data_plot']
		data = json.loads(data_plot)
		data = json.dumps(data['d3'])
		return HttpResponse(data)
	return HttpResponse(status=404)

@login_required(redirect_field_name='login')
def force_csv(request, user):
	response = HttpResponse(content_type='text/csv')
	writer = csv.writer(response)
	data_plot = request.session['data_plot']
	data = json.loads(data_plot)  
	values = []
	writer.writerow(['source', 'target', 'value', 'weight'])
	for x in data['usersInteraction']:
		values.append(x['value'])
	maxim = max(values)
	for x in range(len(data['usersInteraction'])):
		writer.writerow(['Usuario '+str(data['usersInteraction'][x]['receptor']),'Usuario '+str(data['usersInteraction'][x]['emisor']) , float(data['usersInteraction'][x]['value']/maxim),20])
	return HttpResponse(response)
	

@login_required(redirect_field_name='login')
def relations(request, user):
	if user == str(request.user):
		data_plot = request.session['data_plot']
		data = json.loads(data_plot)
		data = json.dumps(data['usersRelation'])
		return HttpResponse(data)
	return HttpResponse(status=404)

@login_required(redirect_field_name='login')
def usersActivity(request):
	data_plot = request.session['data_plot']
	data = json.loads(data_plot)
	data = json.dumps(data['usersActivity'])
	return HttpResponse(data)

@login_required(redirect_field_name='login')
def save_file(request):
	title = 'Generar'
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES, request=request)
		# print(form.is_valid())
		if form.is_valid():
			csv_file = request.FILES["file"]
			file_data = csv_file.read().decode("utf-8")
			plt = ploter.Plot(StringIO(file_data), outputPath=settings.MEDIA_ROOT+'/plot/'+str(request.user))
			request.session['data_plot'] = json.dumps(functions.FillJson(plt, request.POST["name"]))
			file = form.save(commit=False)
			file.user = request.user
			file.save()
			return redirect('/plot/')
	else: 
		form = FileForm()
	return render(request, 'plot/form.html', {'form':form, 'title':title})

@login_required(redirect_field_name='login')
def get_files(request):
	user_files = UserFile.objects.filter(user=request.user)
	title = 'Reportes'
	args = {'user_files':user_files, 'title':title}
	return render(request, 'plot/report_list.html', args)

@login_required(redirect_field_name='login')
def show_graphs(request, filename):
	group = UserFile.objects.get(user=request.user, file = filename)
	filename = os.path.join(settings.MEDIA_ROOT, filename)
	file = open(filename, 'r')
	plt = ploter.Plot(file, outputPath=settings.MEDIA_ROOT+'/plot/'+str(request.user))
	request.session['data_plot'] = json.dumps(functions.FillJson(plt, group.name))
	file.close()
	# plt.UsersInteraction()
	return redirect(reverse("plot"))

@login_required(redirect_field_name='login')
@csrf_exempt
def delete_files(request, name):
	response = UserFile.objects.filter(user=request.user, name=name).delete()
	if(response[0]):
		return HttpResponse(status=200)
	return HttpResponse(status=404)

@login_required(redirect_field_name='login')
def group_plots(request):
	data = []
	if request.method == 'POST':
		groups = []
		groups = request.POST.getlist('groups[]')
		files = []
		for group in groups:
			query = UserFile.objects.get(user=request.user, name=group)
			files.append((query.file.path, group))
		for file, group in files:
			f = open(file, 'r')
			plt = ploter.Plot(f, plot_user_speak=False)
			data.append(functions.FillJson(plt, group))
			f.close()
		request.session['data_plot_groups'] = json.dumps(functions.FillJsonGroups(data))
		return HttpResponse(request.session['data_plot_groups'])
	return render(request, 'plot/group_plot.html', {"data":request.session['data_plot_groups']})

@login_required(redirect_field_name='login')
def group_flare_json(request, user):
	if user == str(request.user):
		data = request.session['data_plot_groups']
		data_plot = json.loads(data)
		data_plot = json.dumps(data_plot['d3'])
		return HttpResponse(data_plot)
	return HttpResponse(status=404)

@login_required(redirect_field_name='login')
def group_intdur_json(request, user):
	if user == str(request.user):
		data = request.session['data_plot_groups']
		data_plot = json.loads(data)
		data_plot = json.dumps(data_plot['treemap_intdur'])
		return HttpResponse(data_plot)
	return HttpResponse(status=404)

@login_required(redirect_field_name='login')
def group_interv_json(request, user):
	if user == str(request.user):
		data = request.session['data_plot_groups']
		data_plot = json.loads(data)
		data_plot = json.dumps(data_plot['treemap_interv'])
		return HttpResponse(data_plot)
	return HttpResponse(status=404)

@login_required(redirect_field_name='login')
def group_volume_json(request, user):
	if user == str(request.user):
		data = request.session['data_plot_groups']
		data_plot = json.loads(data)
		data_plot = json.dumps(data_plot['treemap_volume'])
		return HttpResponse(data_plot)
	return HttpResponse(status=404)

@login_required(redirect_field_name='login')
def group_speak_json(request, user):
	if user == str(request.user):
		data = request.session['data_plot_groups']
		data_plot = json.loads(data)
		data_plot = json.dumps(data_plot['treemap_speak'])
		return HttpResponse(data_plot)
	return HttpResponse(status=404)

@login_required(redirect_field_name='login')
def group_summary_json(request, user):
	if user == str(request.user):
		data = request.session['data_plot_groups']
		data_plot = json.loads(data)
		data_plot = json.dumps(data_plot['summary'])
		return HttpResponse(data_plot)
	return HttpResponse(status=404)


