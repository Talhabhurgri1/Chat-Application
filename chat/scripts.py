from .models import chatUser
from django.core import serializers
from django.contrib.auth.models import User

def get_all_users(request):
    context = {}
    try:
        users = chatUser.objects.all()
    except Exception:
        print("There is something wrong!!")

    context["all_users"] = users
    return context


def get_active_users(request):
    context = {}
    try:
        users = chatUser.objects.filter().exclude(user=request.user)
        users = serializers.serialize("json", users)
    except Exception:
        print("Oops!! Something went wrong!")

    context["active_users"] = users

    return context

def user_additional_details(request):
    context = {}
    try:
        users = User.objects.filter().exclude(id=request.user.id)
        print(users)
        users = serializers.serialize("json", users)
    except Exception:
        print("Oops!! Something went wrong!")

    context["additional_user"] = users
    print(users)
    return context
    
