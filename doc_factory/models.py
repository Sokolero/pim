from django.db import models
from datetime import datetime

# Create your models here.
class EntryModel(models.Model):

    title = models.CharField(max_length=500, blank=True)
    tu = models.CharField(max_length=100, blank=True)
    length = models.CharField(max_length=100, blank=True)
    res = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    adress = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=100, default='В работе')
    notes = models.TextField(max_length=1000, default='')

    contractNumber = models.TextField(max_length=100, default='П-01')
    contractDate = models.DateField(default=datetime.today())
    cost = models.CharField(max_length=100, default='50000.00')

    def __str__(self):
        return self.adress
