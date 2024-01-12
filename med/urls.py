from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_med),
    path('check/', views.check)
]
