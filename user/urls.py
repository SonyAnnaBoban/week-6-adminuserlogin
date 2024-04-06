"""
URL configuration for AdminUserLogin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login_page'),
    path('signup/',views.signup, name='signup_page'),
    path('signout/', views.signout, name='signout'),
    path('adminsignout/', views.adminsignout, name='adminsignout'),
    path('Home/', views.home, name='home_page'),
    path('adminlogin/', views.adminlogin, name='admin'),
    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),
    path('edit/<pk>', views.edit, name='edit'),
    path('delete/<pk>', views.delete, name='delete'),
    path('search/',views.search, name='search'),
]

