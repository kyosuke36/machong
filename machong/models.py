from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    