from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'posts/<int:id>/',
        views.post_detail,
        name='post_detail'
    ),
    path(
        'category/<slug:category_slug>/',
        views.category_posts,
        name='category_posts'
    ),
    path(
        'profile/<slug:username>/',
        views.profile,
        name='profile',
    ),
    path(
        '',
        views.edit_profile,
        name='edit_profile',
    ),
    path(
        'posts/<int:post_id>/comment/',
        views.add_comment,
        name='add_comment',
    ),
    path(
        'posts/<int:post_id>/edit/',
        views.edit_comment,
        name='edit_comment',
    ),
    path(
        'posts/<int:post_id>/delete_comment/<commment_id/',
        views.delete_comment,
        name='delete_comment',
    ),
    path(
        'posts/create/',
        views.create_post,
        name='create_post',
    ),
    path(
        'posts/<int:post_id>/edit/',
        views.edit_post,
        name='edit_post',
    ),
    path(
        'posts/<int:post_id>/delete/',
        views.delete_post,
        name='delete_post',
    ),
]
