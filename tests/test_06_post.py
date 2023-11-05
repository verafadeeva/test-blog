import pytest
from http import HTTPStatus


@pytest.mark.django_db(transaction=True)
class TestPost:
    post_list_url = '/api/v1/posts/'
    post_detail_url = '/api/v1/posts/{post_id}/'

    def test_show_only_published_posts(self, user_client, post1, post2, post3):
        response = user_client.get(self.post_list_url)
        assert len(response.json()) == 2, (
            ('Проверьте, что в выдаче присутствуют только посты с атрибутом'
             ' `is_published=True`')
        )

    def test_show_all_field_in_post(self, user_client, post1):
        post_id = post1.id
        expected_fields = (
            'id', 'author', 'title', 'text', 'is_published', 'created_at'
        )
        response = user_client.get(
            self.post_detail_url.format(post_id=post_id)
        )
        data = response.json()
        for field in expected_fields:
            assert field in data, (
                (f'Проверьте, что поле `{field}` присутствует в сериализаторе '
                 'для поста на выдачу данных')
            )

    def test_create_post_with_invalid_data(self, user_client):
        invalid_data = {
            'title': 'title1'
        }
        response = user_client.post(self.post_list_url, data=invalid_data)
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            'Проверьте, что при создании поста передаются все необходимые поля'
            f' {response.data.serializer.errors}'
        )
