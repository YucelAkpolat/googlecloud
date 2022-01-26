from unicodedata import category
from django.shortcuts import render
from django.template import context
from . models import Category, Urunler,Tag
from blog.models import Post

# Create your views here.
def urunler(request):

    urunler = Urunler.objects.all()
    posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'urunler':urunler,
        'posts':posts,
        'categories':categories,
        'tags':tags
    }
    return render(request,'urunler.html',context)


def urun_detay(request,category_slug,urun_id):
    urun = Urunler.objects.get(category__slug=category_slug, id = urun_id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'urun':urun,
        'tags':tags,
        'categories':categories
    }

    return render(request,'urun_detay.html',context)

def urun_kategory(request,category_slug):
    urunler = Urunler.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'urunler':urunler,
        'tags':tags,
        'categories':categories
    }

    return render(request,'urunler.html',context)

def tag_kategory(request,tag_slug):
    urunler = Urunler.objects.all().filter(tags__slug=tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'urunler':urunler,
        'tags':tags,
        'categories':categories
    }

    return render(request,'urunler.html',context)