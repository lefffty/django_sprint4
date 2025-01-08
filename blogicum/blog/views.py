from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

from datetime import date

from .models import Category, Post, Comment
from .forms import UserForm, CommentForm, PostForm


User = get_user_model()


def index(request):
    """Главная страница проекта"""
    posts = Post.objects.filter(
        pub_date__lte=date.today(),
        is_published__exact=True,
        category__is_published__exact=True,
    ).order_by('-pub_date')

    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(
        request,
        'blog/index.html',
        context,
    )


def category_posts(request, category_slug):
    """Страница отдельной категории"""
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

    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'category': category,
    }

    return render(
        request,
        'blog/category.html',
        context
    )


def post_detail(request, id):
    """Страница отдельной публикации"""
    post = get_object_or_404(
        Post,
        pk=id,
        is_published__exact=True,
        category__is_published__exact=True
    )

    comments = Comment.objects.filter(
        post__exact=id,
    ).order_by('created_at')

    form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }

    return render(
        request,
        'blog/detail.html',
        context,
    )


def profile(request, username):
    """Страница профиля пользователя"""
    user = get_object_or_404(
        User,
        username=username
    )

    posts = Post.objects.filter(
        author_id__exact=user.pk,
    ).order_by('-pub_date')

    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'profile': user,
        'page_obj': page_obj,
    }

    return render(
        request,
        'blog/profile.html',
        context,
    )


def edit_profile(request):
    """Страница редактирования данных пользователя"""
    instance = get_object_or_404(
        User,
        pk=request.user.id,
    )

    form = UserForm(
        request.POST or None,
        instance=instance,
        files=request.FILES or None,
    )

    context = {
        'form': form
    }

    if form.is_valid():
        form.save()

    return render(
        request,
        'blog/user.html',
        context,
    )


def add_comment(request, post_id):
    """Добавление комментария"""
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.post_id = post_id
        comment.save()
        return redirect(
            'blog:post_detail',
            post_id,
        )

    context = {
        'form': form,
    }

    return render(
        request,
        'blog/comment.html',
        context,
    )


def edit_comment(request, post_id, comment_id):
    """Редактирование комментария"""
    instance = get_object_or_404(
        Comment,
        pk=comment_id,
    )

    form = CommentForm(
        request.POST or None,
        instance=instance,
    )

    context = {
        'form': form,
    }

    if form.is_valid():
        form.save()

    return render(
        request,
        'blog/comment.html',
        context,
    )


def delete_comment(request, post_id, comment_id):
    """Удаление комментария"""
    instance = get_object_or_404(
        Comment,
        pk=comment_id,
    )

    form = CommentForm(
        request.POST or None,
        instance=instance,
    )

    if request.method == 'POST':
        instance.delete()
        return redirect(
            'blog:post_detail',
            post_id,
        )

    context = {
        'form': form,
        'comment': instance,
    }

    return render(
        request,
        'blog/comment.html',
        context
    )


def create_post(request):
    """Создание публикации"""
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(
            'blog:profile',
            request.user.username
        )

    context = {
        'form': form,
    }

    return render(
        request,
        'blog/create.html',
        context=context
    )


def delete_post(request, post_id):
    """Удаление публикации"""
    instance = get_object_or_404(
        Post,
        pk=post_id,
    )

    form = PostForm(
        request.POST or None,
        instance=instance,
    )

    if request.method == 'POST':
        instance.delete()
        return redirect(
            'blog:index',
        )

    context = {
        'form': form,
    }

    return render(
        request,
        'blog/create.html',
        context=context,
    )


def edit_post(request, post_id):
    """Редактирование публикации"""
    instance = get_object_or_404(
        Post,
        pk=post_id,
    )

    form = PostForm(
        request.POST or None,
        instance=instance,
        files=request.FILES or None,
    )

    context = {
        'form': form
    }

    if form.is_valid():
        form.save()

    return render(
        request,
        'blog/create.html',
        context=context,
    )
