from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView
from django.http import HttpResponse
import json
# class ShowEmployees(object, ListView):
#   def __str__(self):
#         return self.name


def ShowEmployees(ListView):
	data = Employee.objects.all()
	new_data = []
	for i in range(len(data)):
		new_dict = data[i].__dict__
		new_dict.pop("_state")
		new_data.append(data[i].__dict__)


	return HttpResponse(json.dumps(new_data))




# def ShowEmployees(request):
# 	return HttpResponse("You're looking at question %s." % Employee)
