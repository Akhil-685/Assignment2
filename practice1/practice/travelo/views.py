from django.shortcuts import render
from django.http import HttpResponse
from  .models import menu
# Create your views here.

def home(request):
    menul = menu.objects.all()
    return render(request, 'index.html',{'menul' : menul})