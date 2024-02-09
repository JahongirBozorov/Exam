from django.db import models


class Teacher(models.Model):
    objects = None
    name = models.CharField(max_length=255, default=None)
    course = models.CharField(max_length=255)
    room = models.IntegerField(default=1)
    img = models.ImageField(default=None)
