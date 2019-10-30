from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    dt_creation = models.DateTimeField(auto_now_add=True)

class Transactions(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    notes = models.TextField()