"""pantryhourtracker URL Configuration

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
from django.urls import path, include
from .views import  staff_dash, review, allhours, edithours, deletehours, approvehour, denyhour

urlpatterns = [
    path('dashboard/', staff_dash, name='staff_dash'),
    path('review/', review.as_view(), name='review'),
    path('review/<int:pk>/approve', approvehour, name='approvehour'),
    path('review/<int:pk>/deny', denyhour, name='denyhour'),
    path('records/', allhours.as_view(), name='volunteers'),
    path('records/<int:pk>/update', edithours.as_view(), name='edithours'),
    path('records/<int:pk>/delete', deletehours.as_view(), name='deletehours'),
]
