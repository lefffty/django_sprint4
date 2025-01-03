from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import Category, Post


# Create your views here.

# Главная страница проекта
def index(request):
    posts = Post.objects.filter(
        pub_date__lte=date.today(),
        is_published__exact=True,
        category__is_published__exact=True,
    ).order_by('-pub_date')[:5]

    context = {
        'post_list': posts
    }

    return render(
        request,
        'blog/index.html',
        context,
    )


# Страница отдельной категории
def category_posts(request, category_slug):
    posts = Post.objects.filter(
        category__slug__exact=category_slug,
        is_published__exact=True,
        pub_date__lte=date.today(),
    ).order_by('-pub_date')

    category = get_object_or_404(
        Category,
        slug__exact=category_slug,
        is_published__exact=True,
    )

    context = {
        'post_list': posts,
        'category': category,
    }

    return render(
        request,
        'blog/category.html',
        context
    )


# Страница отдельной публикации
def post_detail(request, id):
    post = get_object_or_404(
        Post,
        pk=id,
        pub_date__lte=date.today(),
        is_published__exact=True,
        category__is_published__exact=True
    )

    context = {
        'post': post
    }

    return render(
        request,
        'blog/detail.html',
        context,
    )
