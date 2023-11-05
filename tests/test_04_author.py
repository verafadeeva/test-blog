import pytest
from http import HTTPStatus


@pytest.mark.django_db(transaction=True)
class TestAuthor:
    post_list_url = '/api/v1/posts/'
    post_detail_url = '/api/v1/posts/{post_id}/'

    def test_update_post_successful(self, author_client, post1):
        data = {
            'title': 'example',
            'text': 'just text',
            'is_published': True
        }
        post_id = post1.id
        response = author_client.put(
            self.post_detail_url.format(post_id=post_id),
            data=data,
        )
        assert response.status_code == HTTPStatus.OK, (
            'Проверьте, что автор может редактировать свои посты'
        )

    def test_delete_post_successful(self, author_client, post1):
        post_id = post1.id
        response = author_client.delete(
            self.post_detail_url.format(post_id=post_id)
        )
        assert response.status_code == HTTPStatus.NO_CONTENT, (
            'Проверьте, что автор может удалять свои посты'
        )
