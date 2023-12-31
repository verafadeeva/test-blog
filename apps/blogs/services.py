import uuid

from django.db import transaction

from apps.blogs.models import Post
from apps.blogs.selectors import get_post
from apps.users.models import CustomUser


@transaction.atomic
def create_post(data: dict, user: CustomUser) -> Post:
    post, is_created = Post.objects.get_or_create(author=user, **data)
    return (post, is_created)


@transaction.atomic
def update_post(id: uuid, data: dict) -> Post:
    post = get_post(id=id)
    for key, value in data.items():
        setattr(post, key, value)
    post.save()
    return post


@transaction.atomic
def delete_post(id: uuid) -> None:
    post = get_post(id=id)
    post.delete()
