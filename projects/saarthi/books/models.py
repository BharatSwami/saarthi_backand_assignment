from django.db import models

# Create your models here.
class table(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)
    isbn = models.CharField(max_length=512)
    authors = models.CharField(max_length=512)
    country = models.CharField(max_length=512)
    numberOfPages=models.CharField(max_length=512)
    publisher=models.CharField(max_length=512)
    release_date=models.CharField(max_length=512)

