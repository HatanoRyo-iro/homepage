from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'iroha/index.html')

def menu(request):
    return render(request, 'iroha/menu.html')

def about(request):
    return render(request, 'iroha/about.html')

def access(request):
    return render(request, 'iroha/access.html')