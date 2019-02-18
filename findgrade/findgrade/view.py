from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def gwa(request):
    return render(request, 'gwa.html')    