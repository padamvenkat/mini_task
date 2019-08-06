from django.contrib import admin
from .models import Data


class Data_collections(admin.ModelAdmin):
    list_display=('sname','ssubject','smarks')





# Register your models here.
admin.site.register(Data,Data_collections)
