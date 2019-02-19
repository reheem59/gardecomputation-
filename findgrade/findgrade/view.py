from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def gwa(request):
	users_instance = users.objects.create(name='test')
    return render(request, 'gwa.html')    