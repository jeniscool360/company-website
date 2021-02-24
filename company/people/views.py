from django.shortcuts import render
from django.http import JsonResponse
from django.conf.global_settings import MEDIA_URL
import requests
from .models import Person, Employee

def generate_image(request):
  # Use this site to generate an image file of a person
  url = 'https://thispersondoesnotexist.com/image'
  req = requests.get(url)
  # Adjust the names and paths below to fit your project
  filename = '/persons/tmp.jpg'
  file = open('media' + filename, 'wb+')
  # Write the file
  for chunk in req.iter_content(100000):
    file.write(chunk)
  file.close()

  return JsonResponse(data={
    "path": MEDIA_URL + filename
  })

def view_people(request):
  people = Person.objects.all()
  return render(request, "people.html", {
    "people" : people
  })

def get_employee_image(request):
  try:
    employee = Employee.objects.get(
      id=int(request.GET["id"])
    )
    return JsonResponse({
      "employee": employee.image.url
    })
  except:
    return JsonResponse({
      "employee": ""
    })