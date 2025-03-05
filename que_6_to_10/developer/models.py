from django.db import models

class developers(models.Model):
    name = models.CharField(max_length=255)
    specialist = models.CharField(max_length=255)
    experience = models.IntegerField()  
    contact = models.CharField(max_length=15)

