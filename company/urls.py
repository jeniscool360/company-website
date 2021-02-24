"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from company.people.views import generate_image, view_people, get_employee_image
from .product import views
from .appointments import views as appt_views

urlpatterns = [
    path('products', views.view_products, name="products"),
    path('appointments', appt_views.AppointmentsView.as_view(), name="appointments"),
    path('admin/', admin.site.urls),
    path('generate-image/', generate_image, name="generate-image"),
    path('', TemplateView.as_view(template_name="index.html")),
    path('people/', view_people, name="people"),
    path('employee', get_employee_image)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)