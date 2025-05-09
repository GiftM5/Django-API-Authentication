from django.urls import path
from .views import login,get_user_emails,create_user,user_details,signup,test_token

urlpatterns = [    
    path('login/',login, name='User_Login'),
    path('signup/',signup, name='User_Login'),
    path('test_token/',test_token, name='User_Login'),
    path('users/',get_user_emails,name = 'user_emails'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_details, name='user_details'),
]
