from django.shortcuts import HttpResponse, redirect, render
from Enroll import models
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer
from .serializers import TempleSerializer
from rest_framework.viewsets import ModelViewSet
from .serializers import TempleSerializer
from .serializers import CategorySerializer
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Q

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

def wapview(request): 
    context = {}
    context ['title'] ="แหล่งรวมวัดจังหวัดศรีสะเกษ"

    by_name = Q()
    by_type = Q()
 
    if request.method == "POST":
        temp_name = request.POST.get('name')
        temp_type = request.POST.get('type')
        
        by_name = Q(name__icontains=temp_name)
        by_type = Q(Category__id=temp_type)

        context['temples'] = models.temple.objects.filter(by_name & by_type)

    else:
        context['temples'] = models.temple.objects.all()

    context['Category'] = models.Category.objects.all()
    
    
    return render(request, 'homepang.html', context)
  
class templeViewSet(generics.ListAPIView):
    serializer_class = TempleSerializer
    def get_queryset(self):
        return models.temple.objects.all()

class templeSelectViewSet(generics.ListAPIView):
    serializer_class = TempleSerializer
    def get_queryset(self):
        temple_id = self.kwargs['templeid']
        return models.temple.objects.filter(id=temple_id)

def mapshow(request):
    context = {
        'title': "แผนที่แสดงวัด",
    }
    return render(request, 'map.html', context)

def templeone(request, id):
    temple = models.temple.objects.get(id=id)
    context = {
        'title': "ข้อมูลที่เลือก",
        'temple': temple,
    }
    return render(request, 'view.html', context)


class templeViewSet(generics.ListAPIView):
    queryset = models.temple.objects.all()
    serializer_class = TempleSerializer

class CategorySerializer(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


