import uuid

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from apps.blogs.models import Post


def get_all_posts() -> QuerySet:
    return Post.objects.select_related('author').filter(is_published=True)


def get_post(id: uuid) -> Post:
    return get_object_or_404(Post, id=id)
