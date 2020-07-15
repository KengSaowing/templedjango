from django.shortcuts import HttpResponse, redirect, render
from Enroll import models
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import TempleSerializer
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.
def Home(request):
    Category_obj = models.Category.objects.all().order_by('-id')[:1]
    temple_obj = models.temple.objects.all().order_by('-id')[:1]
    context = {
        'title': "สรุปจำนวน",
        'Category': Category_obj,
        'temple':temple_obj,

    }
    return render(request, 'home.html', context)
def templeList(request):
    temple_obj = models.temple.objects.all()
    context = {
        'title': "รีวิววัด",
        'temple':temple_obj,
    }    
    return render(request, 'temple.html', context)
def CategoryList(request):
    Category_obj = models.Category.objects.all()
    context = {
        'title': "ข้อมูลประเภทวัด",
        'Category':Category_obj
    }
    return render(request, 'Category.html', context)
def temList(request):
    temple_obj = models.temple.objects.all()
    context = {
        'title': "ตารางวัด",
        'temple': temple_obj,
    }
    return render(request, 'tem.html', context)

def nametemple(request):
    temple_id = request.data.get("templeid")
    temple_obj = models.temple.objects.get(id=temple_id)
    #serializer_class = TempleSerializer
    data = {
        'name': temple_obj.name
    }
    return Response(data)

class templeViewSet(generics.ListAPIView):
    serializer_class = TempleSerializer
    def get_queryset(self):
        return models.temple.objects.all()
    

class CategorySerializer(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer