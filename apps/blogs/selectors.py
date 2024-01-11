import logging
import uuid

from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from apps.blogs.models import Post


logger = logging.getLogger(__name__)


def get_all_posts() -> QuerySet:
    logger.info("Get all posts from data base")
    return Post.objects.select_related('author').filter(is_published=True)


def get_post(id: uuid) -> Post:
    logger.info("Get the post from data base id=%s", id)
    return get_object_or_404(Post, id=id)
