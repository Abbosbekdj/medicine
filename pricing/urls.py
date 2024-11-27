from django.urls import path
from pricing import views

urlpatterns = [
    path('', views.prices, name='prices'),
]
