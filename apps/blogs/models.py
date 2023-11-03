import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)

    class Meta:
        abstract = True


class Post(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    is_published = models.BooleanField()

    class Meta():
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f'{self.author}: {self.title}'
