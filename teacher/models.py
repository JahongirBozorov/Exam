from django.db import models


class Teacher(models.Model):
    objects = None
    name = models.CharField(max_length=255, default=None)
    course = models.CharField(max_length=255)
    room = models.IntegerField(max_length=15, default=1)
    img = models.ImageField(default=None)
