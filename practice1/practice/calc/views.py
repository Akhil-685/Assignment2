from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html',{'name' : 'Akhil'})

def result(request):
    num11 = int(request.POST['num1'])
    num22 = int(request.POST['num2'])
    out = num11+num22
    return render(request,'add.html',{'resu' : out})