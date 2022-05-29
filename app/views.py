from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from subprocess import run, PIPE
import sys
#from .models import Cardata
import csv
sys.path.insert(0,"E:/Desktop/MS-ENGAGE/django/project/app")
from final_anpr import number
from .models import *



def index(request):
    return render(request, 'index.html')

def work(request):
    return render(request,'work.html')


x = number()
def out(request):

    car=Cardata.objects.get(plate=x)

    return render(request,'work.html',{'Cardet': car})












