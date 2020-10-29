from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=20)
    imagelink = models.FilePathField(path="/home/images")
    description = models.CharField(max_length=100)


class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=25)
