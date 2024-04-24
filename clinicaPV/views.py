from django.shortcuts import render

def index(request):
    return render(request, 'clinicaPV/index.html')

def sobre(request):
    return render(request, 'clinicaPV/sobre.html')

def home(request):
    return render(request, 'clinicaPV/index.html')