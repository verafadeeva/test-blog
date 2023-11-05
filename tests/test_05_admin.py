import pytest
from http import HTTPStatus


@pytest.mark.django_db(transaction=True)
class TestAdmin:
    post_list_url = '/api/v1/posts/'
    post_detail_url = '/api/v1/posts/{post_id}/'

    def test_update_post_successful(self, admin_client, post1):
        data = {
            'title': 'example',
            'text': 'just text',
            'is_published': True
        }
        post_id = post1.id
        response = admin_client.put(
            self.post_detail_url.format(post_id=post_id),
            data=data,
        )
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что пользователь с правами админа может редактировать'
            ' любые посты'
        )

    def test_delete_post_successful(self, admin_client, post1):
        post_id = post1.id
        response = admin_client.delete(
            self.post_detail_url.format(post_id=post_id)
        )
        assert response.status_code == HTTPStatus.NO_CONTENT, (
            'Проверьте, что пользователь с правами админа может удалять'
            ' любые посты'
        )
