from django.db import models

# Create your models here.
class Car(models.Model):
    r = [("1day=500","1day=500"),("2day=1000","2day=1000")]
    gen = [("female","femlae"),("male","male")]


    cid = models.IntegerField(primary_key=True)
    c_name = models.CharField(max_length=23)
    c_no = models.BigIntegerField()
    numberplate = models.IntegerField()
    datefrom =  models.DateField()
    dateto = models.DateField()
    rate = models.CharField(max_length=23,choices=r)
    gender = models.CharField(max_length=23,choices=gen)

