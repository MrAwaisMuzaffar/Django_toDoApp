from django.http import HttpResponse
from django.shortcuts import render
from . import views
# Create your views here.

def index(request):
    return render(request, "app1/index.html")
def brian(request):
    return HttpResponse("hello brian")
def david(requst):
    return HttpResponse("david")

def greet(request,name):
    return render(request , "app1/greet.html" , {
      "name":  name.capitalize()
    })

def default(requst):
    return HttpResponse("hello world")