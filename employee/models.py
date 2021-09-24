from django.db import models

class Employee(models.Model):    
	firstName= models.CharField(max_length=200)
	lastName= models.CharField(max_length=200)
	salary= models.PositiveIntegerField()
	department= models.CharField(max_length=200)
	def __str__(self):
		return str(self.__dict__)