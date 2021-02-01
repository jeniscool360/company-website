from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100000000000000000000000)
    description = models.TextField(max_length=100000000000000000000000)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name