from django.db import models

# Create your models here.

class Publisher(models.Model):
    name=models.CharField(max_length=30)
    website=models.URLField()

class Author(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()

class Book(models.Model):
    title=models.CharField(max_length=100)
    authors=models.ManyToManyField(Author)
    Publisher=models.ForeignKey(Publisher)
    publication_date=models.DateField
    