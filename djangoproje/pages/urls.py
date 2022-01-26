from django import views
from django.urls import path
from . import views
from pages.views import AboutView
from pages.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/',  AboutView.as_view(), name='about'),
]
