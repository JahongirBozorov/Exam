from django.db import models


# Create your models here.

class Student(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    date_time = models.CharField(max_length=255)
    attendance = models.DecimalField(max_digits=13, decimal_places=0, default=0)
    room = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    payment = models.DecimalField(max_digits=12, decimal_places=0)
    is_payment = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    course_date = models.CharField(max_length=255, default=0)
