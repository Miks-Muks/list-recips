from django.urls import path
from recip.views import home, recip_detail, categories, recip_delete, recip_of_category

urlpatterns = [
    path('home', home, name='home'),
    path('recip detail/<int:recip_pk>', recip_detail, name='recip_detail'),
    path('categories', categories, name='categories'),
    path('recip delete/<int:recip_pk', recip_delete, name='recip_delete'),
    path('recip of category/<int:categories_pk', recip_of_category, name='recip_of_category'),


]