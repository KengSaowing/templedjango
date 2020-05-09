from django.shortcuts import HttpResponse, redirect, render
from Enroll import models
from django.contrib.auth.models import User

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

def TClist(request):
    templeL_obj = models.temple.objects.all()
    Category_obj = models.Category.objects.all()
    context = {
        'title': "ประเภทวัด/ชื่อวัด",
        'temple': templeL_obj,
        'Category': Category_obj
    }
    return render(request, 'viws.html' , context)