"""temple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# import for display image
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import (login as auth_login,  authenticate)
from rest_framework import routers, serializers, viewsets
from Enroll.views import templeViewSet
from Enroll.views import CategorySerializer,  templeSelectViewSet

router = routers.DefaultRouter()
router.register('api/Category', CategorySerializer)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Enroll.urls')),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/temple', templeViewSet.as_view(), name="get-temple-list"),
    path('api/temple/<int:templeid>', templeSelectViewSet.as_view(), name="get-temple-selected"),
]
# For display Media or Image
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)