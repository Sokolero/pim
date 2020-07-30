from django.db import models

# Create your models here.
class ActsModel(models.Model):
    name = models.CharField(max_length=100, default='OrderNumber')
    num = models.IntegerField()
