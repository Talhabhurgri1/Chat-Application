from django.shortcuts import render
from .models import chatUser
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url="login")
def chat(request):
    return render(request, "index.html")


def login_user(request):

    email = request.POST.get("data[email]")
    password = request.POST.get("data[password]")
    print(email)
    print(password)
    if request.method == "POST":
        user = authenticate(username=email, password=password)
        if not user:
            return JsonResponse({"status": 400})  
        login(request, user)
        return JsonResponse({"status": 200})
    return render(request, "signin.html")


def logout_user(request):
    logout(request)


def signup(request):
    
    username = request.POST.get('data[username]')
    email = request.POST.get('data[email]')
    password1 = request.POST.get('data[password1]')
    try:
        if request.method == 'POST':    
            user_check = chatUser.objects.filter(user__email=email)
            if user_check:
                return JsonResponse({"status": 400})
            else: 
                print("here")      
                new_user = User.objects.create_user(email=email, username=username, password=password1)  
                new_user = chatUser.objects.create(user=new_user)
                new_user.save()
                messages.add_message(request, messages.SUCCESS, "User has been created")
                return JsonResponse({"status": 200})
    except Exception:
        print("in exception")                 
    return render(request, "sign-up.html")


    