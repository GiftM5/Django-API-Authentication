from django.urls import path
from .views import get_user_email

urlpatterns = [
     path('users/',get_user_email, user_email = 'get_user_email')
]
