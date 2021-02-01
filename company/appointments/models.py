from django.db import models

# Create your models here.

class Appointments(models.Model):
    date = models.DateTimeField()

    employee = models.ForeignKey(
        to=Employee,
        on_delete=models.CASCADE
    )

