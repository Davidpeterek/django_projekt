from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Úvodní stránka
    path('', views.seznam_tymu, name='seznam_tymu'),
]

