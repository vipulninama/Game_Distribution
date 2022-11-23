"""Game_Distribution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage',views.homepage,name="homepage"),
    path('',views.showuser,name="showuser"),
    path('Insert',views.Insertuser,name="Insertuser"),
    path('Edit/<int:id>',views.EditUser,name="EditUser"),
    path('Update/<int:id>',views.UpdateUser,name="UpdateUser"),
    path('Delete/<int:id>',views.DelUser,name="DelUser"),  
    path('runQuery',views.runQuery,name="runQuery"),
    path('sortuser',views.sortuser,name="sortuser"),
]
