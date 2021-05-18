"""msh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
    path('', include('mshall.urls')),
    path('gallery/', include('mshall.urls')),
    path('hall_of_fame/', include('mshall.urls')),
    path('noticehn/', include('mshall.urls')),
    path('noticegc/', include('mshall.urls')),
    path('noticemn/', include('mshall.urls')),
    path('noticegn/', include('mshall.urls')),
    path('admin/', admin.site.urls),
]
