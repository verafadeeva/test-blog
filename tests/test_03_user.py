import pytest
from http import HTTPStatus


@pytest.mark.django_db(transaction=True)
class TestUser:
    post_list_url = '/api/v1/posts/'
    post_detail_url = '/api/v1/posts/{post_id}/'

    def test_successful_access_get_all_posts(self, user_client):
        response = user_client.get(self.post_list_url)

        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что GET-запрос авторизованного пользователя к '
            f'`{self.post_list_url}` возвращает ответ со статусом 200.'
        )

    def test_successful_access_get_post(self, user_client, post1):
        post_id = post1.id
        response = user_client.get(
            self.post_detail_url.format(post_id=post_id)
        )

        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что GET-запрос авторизованного пользователя к '
            f'`{self.post_detail_url}` возвращает ответ со статусом 200.'
        )

    def test_create_post_successful(self, user_client):
        data = {
            'title': 'example',
            'text': 'just text',
            'is_published': True
        }
        response = user_client.post(self.post_list_url, data=data)
        assert response.status_code == HTTPStatus.CREATED, (
            'Проверьте, что POST-запрос авторизованного пользователя к'
            f'`{self.post_list_url}` возвращает ответ со статусом 201.'
        )

    def test_update_post_failed(self, user_client, post1):
        data = {
            'title': 'example',
            'text': 'just text',
            'is_published': True
        }
        post_id = post1.id
        response = user_client.put(
            self.post_detail_url.format(post_id=post_id),
            data=data,
        )
        assert response.status_code == HTTPStatus.FORBIDDEN, (
            'Проверьте, что у пользователя нет прав редактировать '
            'чужие посты'
        )

    def test_delete_post_failed(self, user_client, post1):
        post_id = post1.id
        response = user_client.delete(
            self.post_detail_url.format(post_id=post_id)
        )
        assert response.status_code == HTTPStatus.FORBIDDEN, (
            'Проверьте, что у пользователя нет прав удалять '
            'чужие посты'
        )
