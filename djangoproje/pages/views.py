from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from urunler.models import Urunler
from blog.models import Post,Video

# Create your views here.
#def index(request):
   # return render(request,'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['urunler'] = Urunler.objects.filter(available=True).order_by('-tarih')[:4]
        context['posts'] = Post.objects.filter(available=True).order_by('-tarih')[:3]
        context['iframes'] = Video.objects.filter(available=True).order_by('-tarih')[:1]

        return context

class AboutView(TemplateView):
 template_name = 'about.html'

