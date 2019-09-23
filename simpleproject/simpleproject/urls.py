"""simpleproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include

""" In earlier versions of Django before 2.0, one had to use the url() method but In Django 2.0, one use the path() method with path converters to capture URL parameters
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    # including the route from the app (displayinfo)
    path('', include('displayinfo.urls'))
]
