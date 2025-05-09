from django.db import models

# Create your models here.
class User(models.Model):
      age = models.IntegerField(default=18)
      user_email = models.CharField(max_length=50)
    
# So this basically creates the tables for the database   
      def __str__(self):
            return self.user_email
      
