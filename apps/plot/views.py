from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
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
	print(request.user)
	html = '<img class="img-responsive" id="plot_img" src="../media/plot/'+str(request.user)+'users_interaction.png" />'
	print(html)
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
def simple_upload(request):
	if request.method == 'POST' and request.FILES['csv_file']:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'El archivo no tiene extensión CSV')
			return HttpResponseRedirect(reverse("plot:upload_csv"))
		#if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"El archivo es demasiado grande (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("plot:upload_csv"))
		# fs = FileSystemStorage()
		# filename = fs.save(csv_file.name, csv_file)
		# uploaded_file_url = fs.url(filename)
		#print(csv_file.read())
		file_data = csv_file.read().decode("utf-8")
		plt = ploter.Plot(file_data)
		plt.UsersInteraction()
		return render(request, 'plot/plot.html')
	return render(request, 'plot.html')

@login_required(redirect_field_name='login')
def flare_json(request, user):
	data_plot = request.session['data_plot']
	data = json.loads(data_plot)
	#print("data plot",data)
	data = json.dumps(data['d3'])
	return HttpResponse(data)

@login_required(redirect_field_name='login')
def relations(request, user):
	data_plot = request.session['data_plot']
	data = json.loads(data_plot)
	#print("data plot",data)
	data = json.dumps(data['usersRelation'])
	return HttpResponse(data)

@login_required(redirect_field_name='login')
def usersActivity(request):
	data_plot = request.session['data_plot']
	data = json.loads(data_plot)
	#print("data plot",data)
	data = json.dumps(data['usersActivity'])
	return HttpResponse(data)

@login_required(redirect_field_name='login')
def save_file(request):
	print("en save file")
	title = 'Generar'
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES, request=request)
		print(form.is_valid())
		if form.is_valid():
			csv_file = request.FILES["file"]
			file_data = csv_file.read().decode("utf-8")
			plt = ploter.Plot(StringIO(file_data), outputPath='media/plot/'+str(request.user))
			request.session['data_plot'] = json.dumps(functions.FillJson(plt))
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
	filename = os.path.join(settings.MEDIA_ROOT, filename)
	file = open(filename, 'r')
	plt = ploter.Plot(file, outputPath='media/plot/'+str(request.user))
	plt.UsersInteraction()
	return redirect(reverse("plot"))

@login_required(redirect_field_name='login')
def delete_files(request, name):
	UserFile.objects.filter(user=request.user, name=name).delete()
	return redirect(reverse("get_files"))


