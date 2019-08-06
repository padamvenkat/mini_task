from django.contrib import admin
from .models import Student
from .models import Faculty
from .models import Emp
class StudentDetails(admin.ModelAdmin):
    list_display=('name','subject','marks')

class FacultyDetails(admin.ModelAdmin):
    search_field=('fname','subject')
    
class EmpDetails(admin.ModelAdmin):
    list_display=('empid','name','password')


# Register your models here.
admin.site.register(Student,StudentDetails)
admin.site.register(Faculty,FacultyDetails)
admin.site.register(Emp,EmpDetails)