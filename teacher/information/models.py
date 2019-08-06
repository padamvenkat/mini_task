from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    marks=models.IntegerField()

    def __str__(self):
        return self.name
        return self.subject
        return self.marks

class Faculty(models.Model):
    fname=models.CharField(max_length=20)
    subject=models.CharField(max_length=30)

    def __str__(self):
        return self.fname
        return self.subject
    
class Emp(models.Model):
    empid=models.CharField(max_length=30)
    name=models.CharField(max_length=25)
    password=models.CharField(max_length=35)

    def __str__(self):
        return self.empid
        return self.name
        return self.password


