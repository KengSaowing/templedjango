from django.urls import path
from Enroll import views


urlpatterns = [
    path('wapviwe', views.Home, name='wap'),
    path('temple_List', views.templeList, name='temple'),
    path('Category_List',views.CategoryList, name='Category'),
    path('tem_List', views.temList, name='tem'),
    path('',views.wapview,name='home'),
 
]