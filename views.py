import contextlib
from contextvars import Context
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from . models import FirstModel

# Create your views here.

class indexView(ListView):
    template_name = "index.html"
    model = FirstModel
    

    def home(request):
        return render(request, "nikolina.html",{"name": "Navin"})


