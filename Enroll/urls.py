from django.urls import path
from Enroll import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('temple_List', views.templeList, name='temple'),
    path('Category_List',views.CategoryList, name='Category'),
    path('tem_List', views.temList, name='tem'),
 
]