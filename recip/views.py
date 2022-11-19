from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponse
from recip.models import Recip, Category, Comments


# Create your views here.

def home(request):
    recip = Recip.objects.all()
    return render(request, 'recip/home.html', {'recip': recip})


def recip_detail(request, recip_pk):
    recip = Recip.objects.get(pk=recip_pk)
    comments = Comments.objects.filter(recip=recip_pk)
    return render(request, 'recip/recip detail.html', {'recip': recip, 'comments': comments})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'recip/categories.html', {'categories': categories})


def recip_of_category(request, categories_pk):
    category = Category.objects.get(pk=categories_pk)
    recipes = Recip.objects.filter(categories=categories_pk)
    return render(request, 'recip/recip of category.html', {'category': category, 'recip': recipes})


def search_recip(request):
    pass


def recip_delete(request, recip_pk):
    recip = get_object_or_404(Recip, pk=recip_pk).delete()
    return redirect('home')





