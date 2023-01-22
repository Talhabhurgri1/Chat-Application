from django.urls import path 
from . import views 

urlpatterns = [
    path("chat/", views.chat, name="chat"),
    path('login/', views.login_user, name="login"),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.login_user, name="signout"),
    path("get-all-users/", views.get_all_users, name="get_all_users")
    
] 