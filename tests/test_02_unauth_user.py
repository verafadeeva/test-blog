import pytest
from http import HTTPStatus


@pytest.mark.django_db(transaction=True)
class TestUserUnAuth:
    post_list_url = '/api/v1/posts/'
    post_detail_url = '/api/v1/posts/{post_id}/'

    def test_successful_access_get_all_posts(self, guest):
        response = guest.get(self.post_list_url)

        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что GET-запрос неавторизованного пользователя к '
            f'`{self.post_list_url}` возвращает ответ со статусом 200.'
        )

    def test_successful_access_get_post(self, guest, post1):
        post_id = post1.id
        response = guest.get(self.post_detail_url.format(post_id=post_id))

        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что GET-запрос неавторизованного пользователя к '
            f'`{self.post_detail_url}` возвращает ответ со статусом 200.'
        )

    def test_create_post_failed(self, guest):
        data = {
            'title': 'example',
            'text': 'just text',
            'is_published': True
        }
        response = guest.post(self.post_list_url, data=data)
        assert response.status_code == HTTPStatus.UNAUTHORIZED, (
            'Проверьте, что создавать посты может только авторизованный '
            'пользователь'
        )

    def test_update_post_failed(self, guest, post1):
        data = {
            'title': 'example',
            'text': 'just text',
            'is_published': True
        }
        post_id = post1.id
        response = guest.put(
            self.post_detail_url.format(post_id=post_id),
            data=data,
        )
        assert response.status_code == HTTPStatus.UNAUTHORIZED, (
            'Проверьте, что у неавторизованного пользователя нет прав '
            'редактировать посты'
        )

    def test_delete_post_failed(self, guest, post1):
        post_id = post1.id
        response = guest.delete(self.post_detail_url.format(post_id=post_id))
        assert response.status_code == HTTPStatus.UNAUTHORIZED, (
            'Проверьте, что у неавторизованного пользователя нет прав '
            'удалять посты'
        )
