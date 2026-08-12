from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "blog Home page")
def about(request):
    return render(request, "blog About page")