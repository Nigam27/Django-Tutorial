from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, welcome to the blog home page!")

def about(request):
    a = 10 + 50
    return HttpResponse(f"Hello, welcome to the about page! The result of 10 + 50 is {a}.")
