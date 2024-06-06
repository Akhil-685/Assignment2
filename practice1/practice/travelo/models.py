from django.db import models

# Create your models here.
class menu(models.Model):
    name = models.CharField(max_length=50)
    descript = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)