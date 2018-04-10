from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your views here.

def index(request):
	return render(request,'plot/index.html')

def plot(request):	
	return render(request, 'plot/plot.html')

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'plot/index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'plot/index.html')
