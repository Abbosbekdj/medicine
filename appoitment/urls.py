from django.urls import path
from appoitment import views
urlpatterns = [
    path('', views.appotment, name='appoitment')
]
