"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import *
from first_app.views import emp_details, create_emp_details, emp_details_home, delete_emp_details
from update_emp.views import update_emp,update_emp_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello),
    path('home/',home),
    path('emp_details/',emp_details,name="emp_details"),
    path('emp_details_home/',emp_details_home),
    path('emp_details_form/',create_emp_details,name="emp_details_form"),
    path('emp_delete/<pk>',delete_emp_details,name='emp_delete'),
    path('update_emp_page/<pk>',update_emp_page,name="page_update"),
    path('emp_update/<int:pk>/',update_emp, name='emp_update')
]
