from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()


class Location(models.Model):
    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Название места',
    )
    is_published = models.BooleanField(
        default=True,
        blank=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        blank=False,
        verbose_name='Добавлено',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Заголовок',
    )
    description = models.TextField(
        blank=False,
        verbose_name='Описание',
    )
    slug = models.SlugField(
        unique=True,
        blank=False,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; '
        'разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )
    is_published = models.BooleanField(
        default=True,
        blank=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        blank=False,
        verbose_name='Добавлено',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Заголовок',
    )
    text = models.TextField(
        blank=False,
        verbose_name='Текст',
    )
    pub_date = models.DateTimeField(
        blank=False,
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — '
        'можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name='Категория',
    )
    is_published = models.BooleanField(
        default=True,
        blank=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        blank=False,
        verbose_name='Добавлено',
        auto_now_add=True,
    )
    image = models.ImageField(
        'Фото',
        blank=True,
        upload_to='post_images',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        blank=False,
        verbose_name='Текст комментария',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created_at',)
