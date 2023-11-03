from django.db.models import QuerySet

from apps.blogs.models import Post


def get_all_posts() -> QuerySet:
    return Post.objects.select_related('author').filter(is_published=True)
