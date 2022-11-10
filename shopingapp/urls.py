
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.additm,name='additm'),
    path("desply",views.desply,name='desply')

]
