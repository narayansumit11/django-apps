from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("home/", views.home, name="home"),
    path("reports/sumit/", views.reports_sumit, name="reports"),
    path("reports/prem/", views.reports_prem, name="reports"),
    path("reports/chitralekha/", views.reports_chitralekha, name="reports"),
]
