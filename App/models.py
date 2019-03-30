from django.db import models

class UserRegister(models.Model):
    name=models.CharField(max_length=20)
    contact=models.IntegerField()
    email=models.EmailField(primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
