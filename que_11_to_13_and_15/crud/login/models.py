from django.db import models

class crud(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.TextField(max_length=255)
