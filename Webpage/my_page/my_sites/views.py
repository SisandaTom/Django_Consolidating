from django.shortcuts import render
from django.http import  HttpRequest


# a definition to display the home content
def home(request):
    return render(request, "home.html")

