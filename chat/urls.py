from django.urls import path 
from . import views 

urlpatterns = [
    path("chat/", views.chat, name="chat"),
    path('login/', views.login_user, name="login"),
    path("signup/", views.signup, name="signup"),
    
] 