from django.urls import path
from .views import login,get_user_email,create_user,user_details

urlpatterns = [    
    path('users/login',login, name='User_Login'),
    path('users/',get_user_email,name = 'user_emails'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_details, name='user_details'),
]
