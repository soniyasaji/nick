from django.db import models

class Student(models.Model): #Table Definition
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    def __str__(self):
        return self.name



