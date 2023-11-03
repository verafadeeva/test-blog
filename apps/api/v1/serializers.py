from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.blogs.models import Post


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'email')


class PostOutputSerializer(serializers.ModelSerializer):
    """Output сериализатор для постов"""

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


class PostInputSerializer(serializers.Serializer):
    """Input сериализатор для постов"""

    title = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=100)
    is_published = serializers.BooleanField()
