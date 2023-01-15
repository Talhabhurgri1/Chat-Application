from django.shortcuts import render, redirect
from .models import chatUser
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
import json

# Create your views here.

def login_user(request):
    return render(request, "signin.html")

def signup(request):
    
    username = request.POST.get('data[username]')
    email = request.POST.get('data[email]')
    password1 = request.POST.get('data[password1]')
    password2 = request.POST.get('data[password2]')
    
    try:
        if request.method == 'POST':    
            user_check = chatUser.objects.filter(user__email = email)
            if user_check:
                print("in if")
                # messages.add_message(request, messages.SUCCESS, "User already exists")
                return JsonResponse({"status":400})
            else:       
                print("in else")
                new_user = User.objects.create_user(email=email, username=username, password=password1)  
                new_user = chatUser.objects.create(user=new_user)
                new_user.save()
                messages.add_message(request, messages.SUCCESS, "User has been created")
                return JsonResponse({"status": 200})
    except Exception:
        pass                  
    return render(request, "sign-up.html")


    