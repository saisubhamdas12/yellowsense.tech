from django.db import models
from django.core import validators

# Create your models here.
class Time(models.Model):
    time=models.TimeField(primary_key=True)

class Maid_deatails(models.Model):
    time=models.ForeignKey(Time,on_delete=models.CASCADE)
    name=models.CharField(primary_key=100,max_length=100)
    age=models.IntegerField()
    phone_number=models.CharField(max_length=10)
    rating=models.FloatField(default=0)
    Date=models.DateField()

    def __int__(self):
        return self.time


class Booking(models.Model):
    time=models.TimeField()
    name=models.ForeignKey(Maid_deatails,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=10)
    Date=models.DateField()
    rating=models.FloatField(default=0)
