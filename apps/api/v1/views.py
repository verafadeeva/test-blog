from rest_framework import status, views
# from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from apps.api.v1.permissions import IsAuthorOrIsAdmin
from apps.api.v1.serializers import PostOutputSerializer, PostInputSerializer
from apps.blogs.selectors import get_all_posts, get_post
from apps.blogs.services import (create_post, delete_post, update_post)


class ListPostView(views.APIView):
    """Отображение списка опубликованных постов"""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    @extend_schema(auth=[])
    def get(self, request):
        posts = get_all_posts()
        return Response(
            PostOutputSerializer(posts, many=True).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        request=PostInputSerializer,
        responses={201: PostOutputSerializer},
        description='Создание поста',
    )
    def post(self, request):
        serializer = PostInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post, created = create_post(serializer.validated_data, request.user)
        stat = status.HTTP_201_CREATED if created else status.HTTP_200_OK
        return Response(
            PostOutputSerializer(post).data,
            status=stat,
        )

    def get_serializer_class(self):
        return PostOutputSerializer


class PostView(views.APIView):
    """CRUD для модели Post"""

    permission_classes = [IsAuthorOrIsAdmin]

    @extend_schema(auth=[])
    def get(self, request, id=None):
        post = get_post(id)
        return Response(
            PostOutputSerializer(post).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        request=PostInputSerializer,
        description='Изменение поста',
    )
    def put(self, request, id=None):
        post = get_post(id)
        self.check_object_permissions(request, post)
        post = update_post(id, request.data)
        return Response(
            PostOutputSerializer(post).data,
            status=status.HTTP_200_OK,
        )

    def delete(self, request, id=None):
        post = get_post(id)
        self.check_object_permissions(request, post)
        delete_post(id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        return PostOutputSerializer
