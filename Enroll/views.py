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
 
    temp_name = ""
    if request.method == "POST":
        temp_name = request.POST.get('name')
        temp_type = request.POST.getlist('type')
 
        if temp_name !="":
            by_name = Q(name__icontains=temp_name)

        if len(temp_type) > 0:
            for tptype in temp_type:
                by_type |= Q(Category__id=tptype)

        query = models.temple.objects.filter(by_name & by_type)

        context['temples'] = query
    else:
        context['temples'] = models.temple.objects.all()

    context['Category'] = models.Category.objects.all()
    
    return render(request, 'webview.html', context)

def Results(request):
    by_name = Q()
    by_type = Q()
 
    temp_name = ""
    query = ""

    if request.method == "POST":
        temp_name = request.POST.get('name')
        temp_type = request.POST.getlist('type')

        print(temp_type)
 
        if temp_name !="":
            by_name = Q(name__icontains=temp_name)

        if len(temp_type) > 0:
            for tptype in temp_type:
                by_type |= Q(Category__id=tptype)

        query = models.temple.objects.filter(by_name & by_type)

    context = {
        "temples": query,
    }
    
    context ['title'] ="ผลลัพธ์ของวัดที่ค้นหาได้"
    

    return render(request, 'Results.html', context)

class templeViewSet(generics.ListAPIView):
    serializer_class = TempleSerializer
    def get_queryset(self):
        return models.temple.objects.all()

class templeSelectViewSet(generics.ListAPIView):
    serializer_class = TempleSerializer
    def get_queryset(self):
        temple_id = self.kwargs['templeid']
        return models.temple.objects.filter(id=temple_id)


def templeone(request, id):
    temple = models.temple.objects.get(id=id)
    context = {
        'title': "ข้อมูลที่เลือก",
        'temple': temple,
    }
    return render(request, 'view.html', context)

def multiplepoint(request):
    temple_obj = models.temple.objects.all()
    locations = []

    for i, temple in enumerate(temple_obj):
        dt = [
            temple.name,
            float(temple.latitude),
            float(temple.Longitude),
            int(i+1),
            str(i+1)
            ]
        locations.append(dt)

    context ={
        "title": " แผนที่แสดงวัด",
        "temple": temple_obj,
        "locations":locations,
    }
    print(locations)
    return render(request, 'multiplepoint.html', context)

def multiplepoint_route(request):
    temple_obj = models.temple.objects.all()
    locations = []

    for i, temple in enumerate(temple_obj):
        
        dt = [
            temple.name,
            float(temple.latitude),
            float(temple.Longitude),
            int(i+1),
            str(i+1)
            ]
        locations.append(dt)
    context ={
        "title": " แผนที่แสดงวัด",
        "locations":locations,
        
    }
    return render(request, 'multiplepoint_route.html', context)

def GetDirection(request, id):
    temple = models.temple.objects.get(id=id)
    if request.method == "POST":
        if request.POST.get('lat') == "":
           latitude = request.POST.get("latitude")
           longitude = request.POST.get("longitude")
        else:
            latitude = 15.1181967
            longitude = 104.3617369
    context ={
        "title": " แผนที่แสดงวัด",
        "temple": temple,
        
    }
    return render(request, 'GetDirection.html', context)

def marker(request):
     context ={
        "title": " แผนที่แสดงวัด",
    }
     return render(request, 'marker.html', context)

def search(request):
     context ={
        "title": " แผนที่แสดงวัด",
    }
     return render(request, 'search.html', context)

    
class templeViewSet(generics.ListAPIView):
    queryset = models.temple.objects.all()
    serializer_class = TempleSerializer

class CategorySerializer(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


