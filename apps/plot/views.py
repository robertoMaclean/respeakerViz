from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import csv
import apps.plot.plot as ploter
import json 
import apps.plot.functions as functions
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.decorators import login_required
import os
from django.core.files import File

# Create your views here.
data_plot = ''
@login_required(redirect_field_name='login')
def index(request):
	if request.method == 'POST':
		filepath = request.FILES.get('csv_file', False)
		if filepath:
			#print(request.FILES['csv_file'])
			csv_file = request.FILES["csv_file"]
			if not csv_file.name.endswith('.csv'):
				messages.error(request,'El archivo no tiene extensión CSV')
				return redirect(reverse("upload_file"))
			#if file is too large, return
			if csv_file.multiple_chunks():
				messages.error(request,"El archivo es muy grande (%.2f MB)." % (csv_file.size/(1000*1000),))
				return redirect(reverse("upload_file"))
			
			# fs = FileSystemStorage()
			# filename = fs.save(csv_file.name, csv_file)
			# uploaded_file_url = fs.url(filename)
			#print(csv_file.read())
			file_data = csv_file.read().decode("utf-8")
			plt = ploter.Plot(file_data)
			#print('tiempo total '+plt.GetTime())
			#print(plt.GetUserTime())
			#print(plt.GetSpeakTime())
			#print(plt.GetUsersInterv()[3])
			
			global data_plot
			data_plot = json.dumps(functions.FillJson(plt))
			return redirect('plot/')
		else:
			messages.error(request,'No ha seleccionado ningun archivo')
			return redirect(reverse("upload_file"))
	return render(request, 'plot/index.html')

@login_required(redirect_field_name='login')
def plot(request):	
	#print(request.session.get['data'])
	global data_plot
	return render(request, 'plot/plot.html',{"data":data_plot})

@login_required(redirect_field_name='login')
def interactions(request):
	html = '<img class="img-responsive" id="plot_img" src="../media/plot/users_interaction.png" />'
	return HttpResponse(html)

@login_required(login_url='accounts/login/')
def interv(request):
	html = '<img class="img-responsive" id="plot_img" src="../media/plot/users_speak.png" />'
	return HttpResponse(html)

@login_required(redirect_field_name='login')
def bar_graph(request):
	html = '<div id="graph" class="graph"></div>'
	global data_plot
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
	global data_plot
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
def flare_json(request):
	global data_plot
	data = json.loads(data_plot)
	#print("data plot",data)
	data = json.dumps(data['d3'])
	return HttpResponse(data)

@login_required(redirect_field_name='login')
def relations(request):
	global data_plot
	data = json.loads(data_plot)
	#print("data plot",data)
	data = json.dumps(data['usersRelation'])
	return HttpResponse(data)

@login_required(redirect_field_name='login')
def usersActivity(request):
	global data_plot
	data = json.loads(data_plot)
	#print("data plot",data)
	data = json.dumps(data['usersActivity'])
	return HttpResponse(data)

def download_file(request):
	path_to_file = os.path.realpath("media/plot/relaciones.csv")
	f = open(path_to_file, 'r')
	myfile = File(f)
	response = HttpResponse(myfile, content_type='application/csv')
	response['Content-Disposition'] = 'attachment; filename=' + "file.csv"
	return HttpResponse(response)



