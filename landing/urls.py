from django.urls import path
from . import views
from .views import robots_view

urlpatterns = [
    path('robots.txt', robots_view, name='robots'),
    path('', views.home, name='home'),
]
