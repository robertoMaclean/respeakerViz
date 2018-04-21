from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import csv
import apps.plot.plot as ploter
import json 
import apps.plot.functions as functions
from django.contrib import messages
from django.urls import reverse

# Create your views here.
data_plot = ''

def index(request):
	if request.method == 'POST' and request.FILES['csv_file']:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return redirect(reverse("upload_file"))
		#if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
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
		#return render(request, 'plot/plot.html')
	return render(request, 'plot/index.html')

def plot(request):	
	#print(request.session.get['data'])
	global data_plot
	return render(request, 'plot/plot.html',{"data":data_plot})

def interactions(request):
	html = '<img class="img-responsive" id="plot_img" src="../media/plot/users_interaction.png" />'
	return HttpResponse(html)

def interv(request):
	html = '<img class="img-responsive" id="plot_img" src="../media/plot/users_speak.png" />'
	return HttpResponse(html)

def bar_graph(request):
	html = '<div id="graph" class="graph"></div>'
	global data_plot
	return HttpResponse(json.dumps({
		"data": data_plot,
		"html": html
		}),
		content_type="aplication/json"
	)

def line_graph(request):
	html = '<div id="line" class="graph"></div>'
	return HttpResponse(json.dumps({
		"data": data_plot,
		"html": html
		}),
		content_type="aplication/json"
	)

def donut_graph(request):
	html = '<div id="donut" class="graph"></div>'
	global data_plot
	return HttpResponse(json.dumps({
		"data": data_plot,
		"html": html
		}),
		content_type="aplication/json"
	)


def simple_upload(request):
	if request.method == 'POST' and request.FILES['csv_file']:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("myapp:upload_csv"))
		#if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("myapp:upload_csv"))
		# fs = FileSystemStorage()
		# filename = fs.save(csv_file.name, csv_file)
		# uploaded_file_url = fs.url(filename)
		#print(csv_file.read())
		file_data = csv_file.read().decode("utf-8")
		plt = ploter.Plot(file_data)
		plt.UsersInteraction()
		return render(request, 'plot/plot.html')
	return render(request, 'plot.html')
