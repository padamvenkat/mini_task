from django.db import models

# Create your models here.
class Data(models.Model):
    sname=models.CharField(max_length=50)
    ssubject=models.CharField(max_length=40)
    smarks=models.CharField(max_length=20)

    def __str__(self):
        return self.sname
        return self.ssubjects
        return self.smarks















