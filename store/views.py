from django.shortcuts import render
from django.http import HttpResponse
from store.models import *
# Create your views here.
def home(request):
    store=coffee.objects.all()
    return render(request,'home.html',{'coffee':store})
