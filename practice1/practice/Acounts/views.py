from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def logout(request):
        auth.logout(request)
        return redirect('/')

def login(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']

                user = auth.authenticate(username = username, password = password)
                if user is not None:
                        auth.login(request, user)
                        return redirect('/')
                else:
                        messages.info(request, 'invalid Credentials')
                        return render(request, 'login.html')
        else:
                return render(request, 'login.html')


def register(request):
        if request.method == 'POST':
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                email = request.POST['email']
                username = request.POST['username']
                password1 = request.POST['password1']
                password2 = request.POST['password2']
                if User.objects.filter(email = email).exists():
                        messages.info(request, 'Account is created with this mail')
                        messages.info(request, 'Use Login')
                        return render(request, 'registration.html')

                elif User.objects.filter(username = username).exists():
                        messages.info(request, 'User Name is Taken Try another')
                        return render(request, 'registration.html')
                else:
                        if password1 == password2:
                                user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password1)
                                user.save();
                                messages.info(request, 'Account Created')
                                return redirect('/')
                        else:
                                messages.info(request, 'Your Password is not Same Re-enter Password')
                                return render(request, 'registration.html')

        else:
                return render(request, 'registration.html')
