from django.shortcuts import render
from .models import chatUser
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.

def login_user(request):
    return render(request, "signin.html")

def signup(request):
    
    username = request.POST.get('data[username]')
    print(username)
    email = request.POST.get('data[email]')
    password1 = request.POST.get('data[password1]')
    password2 = request.POST.get('data[password2]')
    
    try:
        user_check = chatUser.objects.get(user__email = email)
        if user_check:
            return JsonResponse(f"user with {email} already exists")
    except Exception:
        if request.method == 'POST':
            print("here")
            new_user = User.objects.create_user(email=email, username=username, password=password1)  
            new_user = chatUser.objects.create(user=new_user)
            new_user.save()

    return render(request, "sign-up.html")


    