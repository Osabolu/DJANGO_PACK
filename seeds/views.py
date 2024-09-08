from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def seeds(request):
    # return HttpResponse("<h2>Find a suitable soil first to determine<br>weither it's compactible with your hybrid seeds<br/><h2/>")
    return render(request, "seed/seed.html")
