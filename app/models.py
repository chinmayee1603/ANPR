from django.db import models

regno=500
class Cardata(models.Model):
    name = models.CharField(max_length=40)
    state = models.CharField(max_length=20)
    plate = models.CharField(max_length=20)
    regno=models.BigIntegerField

class Bankdetails(models.Model):
    name = models.CharField(max_length=40)
    accno = models.CharField(max_length=12)
    tmoney = models.CharField(max_length=5)

class chalan(models.Model):
    oname=models.CharField(max_length=40)
    amount=models.CharField(max_length=40)
    oplate=models.CharField(max_length=40)
    ostate=models.CharField(max_length=40)

