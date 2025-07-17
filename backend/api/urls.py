from django.urls import path
from .views import create_sweet

urlpatterns = [
    path('sweet/', create_sweet),
]
