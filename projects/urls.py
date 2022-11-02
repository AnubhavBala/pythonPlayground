from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path("",views.project_idx, name="project_idx"),
   path("<int:pk>/", views.project_dtl, name = "project_dtl"),
]