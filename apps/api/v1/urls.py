from django.urls import path

from apps.api.v1.views import ListPostView


urlpatterns = [
    path('posts/', ListPostView.as_view(), name='posts'),
]
