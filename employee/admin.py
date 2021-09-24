from django.contrib import admin
from django.views.generic import ListView
from .models import Employee

admin.site.register(Employee)


class Employee(ListView):
	model = Employee
 