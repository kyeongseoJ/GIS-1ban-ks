from django.db import models

# Create your models here.
class BonBon(models.Model):
    text = models.CharField(max_length=225, null=False)
