from rest_framework import serializers
from .models import User

# We  want to transform our model into json format.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
          model = User
          fields = '__all__'