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
from django.urls import path, include
from .views import individual_report, individual_report_printable, day_report_request, day_report, day_report_printable

urlpatterns = [
    path('individual_report/', individual_report, name='individual_report'),
    path('individual_report/printable/', individual_report_printable, name='individual_report_printable'),
    path('day_report/request', day_report_request, name='day_report_request'),
    path('day_report/', day_report, name='day_report'),
    path('day_report/printable/', day_report_printable, name='day_report_printable'),
]
