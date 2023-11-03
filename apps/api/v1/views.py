from rest_framework import status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

# from apps.api.v1.permissions import IsAuthorOrReadOnly
from apps.api.v1.serializers import PostSerializer
from apps.blogs.selectors import get_all_posts


class ListPostView(views.APIView):
    permission_classes = (AllowAny,)

    @extend_schema(auth=[])
    def get(self, request):
        posts = get_all_posts()
        return Response(
            PostSerializer(posts, many=True).data,
            status=status.HTTP_200_OK,
        )

    def get_serializer_class(self):
        return PostSerializer
