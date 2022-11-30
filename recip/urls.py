from django.urls import path
from .views import (
    RecipDetailView,
    RecipCreateView,
    RecipUpdateView,
    RecipDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recip/<int:pk>/', RecipDetailView.as_view(), name='recip-detail'),
    path('recip/new/', RecipCreateView.as_view(), name='recip-create'),
    path('recip/<int:pk>/update/', RecipUpdateView.as_view(), name='recip-update'),
    path('recip/<int:pk>/delete/', RecipDeleteView.as_view(), name='recip-delete'),
    path('about/', views.about, name='about'),
]