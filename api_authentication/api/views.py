from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

# Create your views here.

@api_view(['GET'])
def get_user_email(request):
    data = {"user_email":"gift@gmail.com","user_id":34}
    serializer = UserSerializer(data)
    return Response(serializer.data)