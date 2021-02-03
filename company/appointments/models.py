from django.db import models
from ..people.models import Employee

# Create your models here.

class Appointments(models.Model):
    date = models.DateTimeField()

    employee = models.ForeignKey(
        to=Employee,
        on_delete=models.CASCADE
    )

