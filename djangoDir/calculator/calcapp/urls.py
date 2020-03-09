from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calc_view, name='calc_view')
]
