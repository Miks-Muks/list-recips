from django.shortcuts import render
from django.http import HttpResponse
from recip.models import Recip, Category, Comments


# Create your views here.

def home(request):
    recip = Recip.objects.all()
    return render(request, 'recip/home.html', {'recip': recip})
