from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


def get_published_posts():
    """Возвращает опубликованные посты с фильтрацией по дате и флагам."""
    return Post.objects.select_related(
        'author', 'category', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    """Главная страница с последними 5 публикациями."""
    post_list = get_published_posts()[:5]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    """Страница отдельной публикации."""
    post = get_object_or_404(
        Post.objects.select_related('author', 'category', 'location'),
        pk=id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Страница категории со всеми её публикациями."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = category.posts.select_related(
        'author', 'location'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now()
    )

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, 'blog/category.html', context)
