from django.shortcuts import render

from . models import Category, Post,Tag


# Create your views here.
def blog(request):

    posts = Post.objects.all().filter(available=True).order_by('-tarih')
    
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'posts':posts,
        'categories':categories,
        'tags':tags,
        
    }
    return render(request,'blog.html',context)











def blog_detay(request,category_slug,post_id):
    post = Post.objects.get(category__slug=category_slug, id = post_id)
    posts = Post.objects.all().filter(available=True).order_by('-tarih')
    
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'posts':posts,
        'post':post,
        'tags':tags,
        'categories':categories
    }

    return render(request,'blog_detay.html',context)

def blog_kategory(request,category_slug):
    posts = Post.objects.all().filter(category__slug=category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'posts':posts,
        'tags':tags,
        'categories':categories
    }

    return render(request,'blog.html',context)

def tag_kategory(request,tag_slug):
    posts = Post.objects.all().filter(tags__slug=tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'posts':posts,
        'tags':tags,
        'categories':categories
    }

    return render(request,'blog.html',context)