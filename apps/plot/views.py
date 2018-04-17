from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import csv
import apps.plot.plot as ploter
import json 
import apps.plot.functions as functions

# Create your views here.
data_plot = ''

def index(request):
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
		print('tiempo total '+plt.GetTime())
		print(plt.GetUserTime())
		print(plt.GetSpeakTime())
		print(plt.GetUsersInterv()[3])
		usersTime = plt.GetUserTime()
		data = {
				'users':[]
				}
		user_num = 1
		for users in usersTime:
			data['users'].append({'x':'Usuario '+str(user_num),'y':users})
			user_num += 1
		data = json.dumps(data)	
		global data_plot
		data_plot = json.dumps(functions.FillJson(plt))
		return redirect('plot/')
		#return render(request, 'plot/plot.html')
	return render(request, 'plot/index.html')

def plot(request):	
	#print(request.session.get['data'])
	global data_plot
	return render(request, 'plot/plot.html',{"data":data_plot})

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
