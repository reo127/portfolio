from enum import auto
from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    massage = models.TextField()
    timeStamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
