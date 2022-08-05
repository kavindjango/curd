from django.db import models

# Create your models here.
class datas(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.CharField(max_length=20)
    Contact=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
