from django.contrib import admin
from .models import Employee, Testimonial
from django.db import models
from django.forms.widgets import ClearableFileInput # This is what ImageFields use by default, we're going to customize ours a little.

class ImageWidget(ClearableFileInput):
  template_name = "image_widget.html"

class PersonAdmin(admin.ModelAdmin):
  formfield_overrides = {
    models.ImageField: {'widget': ImageWidget},
  }

admin.site.register(Employee, PersonAdmin)
admin.site.register(Testimonial, PersonAdmin)

