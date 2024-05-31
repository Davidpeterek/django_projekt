from django.urls import path
from . import views

urlpatterns = [
    path('tymy/', views.seznam_tymu, name='seznam_tymu'),
]

