from django.db import models
from django.db.models import Model, ForeignKey, CharField, IntegerField


class Product(models.Model):
    name = CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
         return self.name

class User(models.Model):
    name = CharField(max_length=100)
    def __str__(self):
         return self.name

class Voting(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE)
    product = ForeignKey(Product, on_delete=models.CASCADE)
    stars = IntegerField()


