from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Recip


def home(request):
    recip = Recip.objects.all()
    context = {
        'recip': recip,
    }
    return render(request, 'recip/home.html', context)


class RecipDetailView(DetailView):
    model = Recip


class RecipCreateView(LoginRequiredMixin, CreateView):
    model = Recip
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Recip
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class RecipDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Recip
    success_url = '/'

    def test_func(self):
        recip = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'О сайте'})



