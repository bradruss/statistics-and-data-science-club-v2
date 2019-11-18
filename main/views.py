from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def people(request):
    return render(request, 'main/people.html')

def software(request):
    return render(request, 'main/software.html')

def links(request):
    return render(request, 'main/links.html')

def asa(request):
    return render(request, 'main/asa.html')

def handler404(request, *args, **kwargs):
    return render(request, 'main/404.html', status=404)

def handler500(request):
    return render(request, 'main/500.html', status=500)
