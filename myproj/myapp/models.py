from django.db import models

# Create your models here.
class Feature(models.Model):
    name: models.CharField(max_length=100) # str
    details: models.CharField(max_length=500) #str
    # is_trus:# bool
    # id: int dont need an idea bc models auto have one (need the (models.Model))



    # anytime you change smth in this file you have to do python3 manage.py makemigrations, then python3 manage.py migrate