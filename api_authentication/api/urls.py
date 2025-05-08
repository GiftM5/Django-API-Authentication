from django.urls import path
from .views import get_user_email

urlpatterns = [
     path('user/',get_user_email, email = 'get_user_email')
]
