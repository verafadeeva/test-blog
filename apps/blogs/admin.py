from django.contrib import admin

from apps.blogs.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title", "is_published")
    empty_value_display = "-пусто-"
