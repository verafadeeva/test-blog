from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.blogs.models import Post


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'email')


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'text',
            'is_published',
            'created_at',
        )
