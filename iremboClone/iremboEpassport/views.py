
from django.shortcuts import render
from django.template  import loader

def index(request):
    return render(request, "iremboEpassport/index.html")
