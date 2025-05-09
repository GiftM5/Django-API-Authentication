from django.urls import path
from .views import get_user_email, create_user,user_details

urlpatterns = [    
    path('users/', get_user_email, name='get_user_email'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_details, name='user_details'),
]
