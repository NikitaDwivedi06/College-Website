from django.views import generic
from django.shortcuts import render

def show_sitehome(request):
    return render(request, 'SE/sitehome.html')
