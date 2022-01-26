from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.urunler, name='urunler'),
    path('<slug:category_slug>/<int:urun_id>', views.urun_detay, name='urun_detay'),
    path('categories/<slug:category_slug>', views.urun_kategory, name='uruns_by_kategory'),
    path('tags/<slug:tag_slug>', views.tag_kategory, name='tags_by_kategory'),
   
]