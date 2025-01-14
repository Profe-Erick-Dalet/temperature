"""temperature URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mediciones.views import (
    AreaAPIListView,
    AreaAPICreateView,
    RegionAPIListView,
    RegionAPICreateView,
    MeasurmentsAPIListView,
    MeasurmentsAPICreateView,

)

urlpatterns = [
    path('areas/',AreaAPIListView.as_view(),name='areas-list'),
    path('areas/create',AreaAPICreateView.as_view(),name='areas-create'),
    #---------
    path('regiones/',RegionAPIListView.as_view(),name='regiones_list'),
    path('regiones/create',RegionAPICreateView.as_view(),name='regiones_create'),
    #---------
    path('measurments/',MeasurmentsAPIListView.as_view(),name='measurments_list'),
    path('measurments/create',MeasurmentsAPICreateView.as_view(),name='measurments_create'),


    path('admin/', admin.site.urls),

]
