import pytest

from apps.blogs.models import Post


@pytest.fixture
def posts_factory(db, author):
    def create_post(
        title: str,
        text: str = "this is a post's text",
        is_published: bool = True,
    ) -> Post:
        post = Post.objects.create(
            author=author,
            title=title,
            text=text,
            is_published=is_published
        )
        return post
    return create_post


@pytest.fixture
def post1(db, posts_factory) -> Post:
    return posts_factory('title1')


@pytest.fixture
def post2(db, posts_factory) -> Post:
    return posts_factory('title2')


@pytest.fixture
def post3(db, posts_factory) -> Post:
    return posts_factory('title1', is_published=False)
