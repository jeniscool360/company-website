from django.shortcuts import render
from django.views.generic import View
from .forms import AppointmentForm

# Create your views here.

class AppointmentsView(View):

    def get(self, request):
        form = AppointmentForm()

        return render(request, "appointments.html", {
            "form": form
        })

    def post(self, request):
        form = AppointmentForm(request.POST)

        if form.is_valid():
            # save Appointment to database and  instance var
            instance = form.save()

            return render(request, "appointments.html", {
                "form": form,
                "submitted": instance.__str__()
            })
        else:
            return render(request, "appointments.html", {
                "form": form,
                "errors": form.errors
            })