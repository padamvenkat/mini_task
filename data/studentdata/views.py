from django.shortcuts import render
from .models import Data
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
# Create your views here.
class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields=('sname','ssubject','smarks')
@api_view(["GET"])
def api_all(request):
        obj=Data.objects.all()
        if obj:
            rest=DataSerializer(obj,many=True)
            return Response(rest.data)
        else:
            return Response("no data found")