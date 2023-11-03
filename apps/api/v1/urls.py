from django.urls import include, path

from apps.api.v1.views import ListPostView, PostView


urlpatterns = [
    path('auth/', include("djoser.urls.jwt")),
    path('posts/<uuid:id>/', PostView.as_view(), name='post'),
    path('posts/', ListPostView.as_view(), name='posts'),
]
