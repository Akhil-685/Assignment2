from django.db import models

# Create your models here.
class Acounts(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    Email = models.CharField(max_length= 50)
    user_name = models.CharField(max_length= 50)
