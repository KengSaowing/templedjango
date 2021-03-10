from django.urls import path
from Enroll import views


urlpatterns = [
    path('wapviwe',views.Home,name='wap'),
    path('temple_List', views.templeList, name='temple'),
    path('Category_List',views.CategoryList, name='Category'),
    path('tem_List', views.temList, name='tem'),
    path('', views.wapview, name='home'),
    path('multiplepoint',views.multiplepoint,name='multiplepoint'),
    path('templeone/<int:id>',views.templeone,name='templeone'),
    path('multiplepoint_route',views.multiplepoint_route,name='multiplepoint_route'),
    path('GetDirection/<int:id>',views.GetDirection,name='GetDirection'),
    path('marker',views.marker,name='marker'),
    path('Results',views.Results,name='Results'),
    path('ds',views.ds,name='ds'),
    
    
    
 

 
]