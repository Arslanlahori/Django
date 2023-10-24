from django.db import models

class myinfo(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    id_no=models.IntegerField()
    ideas=models.TextField()


# Create your models here.
