from django.urls import path
from .views import (
    RecipListView,
    RecipDetailView,
    RecipCreateView,
    RecipUpdateView,
    RecipDeleteView
)
from . import views

urlpatterns = [
    path('', RecipListView.as_view(), name='recip-home'),
    path('recip/<int:pk>/', RecipDetailView.as_view(), name='recip-detail'),
    path('recip/new/', RecipCreateView.as_view(), name='recip-create'),
    path('recip/<int:pk>/update/', RecipUpdateView.as_view(), name='recip-update'),
    path('recip/<int:pk>/delete/', RecipDeleteView.as_view(), name='recip-delete'),
    path('about/', views.about, name='blog-about'),
]