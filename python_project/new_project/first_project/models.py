from django.db import models
from datetime import datetime

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000 ,blank=True)
    date = models.DateTimeField(default=datetime.now ,blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    

    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title
