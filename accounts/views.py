from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.db import IntegrityError
from django.http import HttpResponse;
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django import forms

# Create your views here.

def manual_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username, password = password)

        if user is not None:
            auth_login(request, user);
            return redirect('note_list')
        else:
            return render(request,'accounts/manual_login.html',{'error' : "credentials are not Valid"})
            
    return render(request, 'accounts/manual_login.html')


# this is for the  logout setup 


def manual_logout(request):
    if request.method == 'POST':
         auth_logout(request)
         return redirect('manual_login')
    return render(request,'accounts/manual_logout.html')

     


# this if for the sign up forming 

def manual_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username','').strip()
        email = request.POST.get('email').strip()

        password1 = request.POST.get('password1','')
        password2 = request.POST.get('password2','')


        # basic checks

        if not username  or not email or not password1 or not password2:
            return render (request, 'accounts/manual_signup.html',{'error' : "Please fill all the fields."})
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'accounts/manual_signup.html',{'error' : "Password did not match.."})
        
        if User.objects.filter(email = email).exists():
              return render(request, 'accounts/manual_signup.html', {'error': 'email  already in use '})
        try:
            user =  User.objects.create_user(username= username,password= password1)
           
        except IntegrityError:
             
             return render(request, 'accounts/manual_signup.html', {'error': "Username already taken."})
        
        auth_login(request, user)
        return redirect('note_list')


    
    return render(request, 'accounts/manual_signup.html')








# this is for the password reset
