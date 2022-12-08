from django.db import models
from django.db.models import Model


# Create your models here.

class Catagories(models.Model):
    category = models.CharField(max_length=250)
    des = models.TextField()

    def __str__(self):
        return(self.category)

class Achievements(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    image = models.ImageField(upload_to="certs")
    url = models.CharField(max_length=500)
    category = models.ForeignKey(Catagories,on_delete=models.CASCADE)

    def __str__(self):
        return(self.name)

class User_Comments(models.Model):
    name = models.CharField(max_length=250, blank=True)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return(self.name)

class Project(models.Model):
    category = models.CharField(max_length=250, blank=True)
    name = models.CharField(max_length=250, blank=True)
    date = models.DateField()
    url = models.URLField(max_length=550)
    desc = models.TextField()
    icon = models.ImageField(upload_to='icons')
    image = models.ImageField(upload_to='projectimages')

    def __str__(self):
        return(self.name)
