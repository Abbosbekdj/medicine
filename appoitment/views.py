from django.shortcuts import render

# Create your views here.

def appotment(request):
    return render(request, 'appointment.html')