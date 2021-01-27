from django.db import models

# Create your models here.
# OwO

class Person(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True)

    class Meta:
        abstract = True

class Employee(Person):
    pass

class Testimonial(Person):
    description = models.TextField(max_length=500)

