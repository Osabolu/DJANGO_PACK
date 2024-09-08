from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def farming(request):
    # return HttpResponse("<h1>What is farming?<h1/>")
    return render(request, "farm/farm.html")
