from django.db import models
from ..people.models import Employee

# Create your models here.

class Appointments(models.Model):
    date = models.DateTimeField()

    employee = models.ForeignKey(
        to=Employee,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"""
        Appointment confirmed for \
        {self.date.strftime('%B %d, %Y, %I:%M %p')} \
        with {self.employee.__str__()}
        """