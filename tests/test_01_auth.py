import pytest
from http import HTTPStatus


@pytest.mark.django_db(transaction=True)
class TestAuth:
    url = '/api/v1/auth/jwt/create/'

    def test_jwt_create_with_no_data(self, guest):
        response = guest.post(self.url)
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            'Убедитесь, что POST-запрос без необходимых данных, отправленный '
            f'к `{self.url}`, возвращает ответ со статусом код 400.'
        )

    def test_jwt_create_with_no_exist_user(self, guest):
        invalid_data = {
            'email': 'invalid_username_not_exists',
            'password': 'invalid pwd'
        }
        response = guest.post(self.url, data=invalid_data)
        assert response.status_code == HTTPStatus.UNAUTHORIZED, (
            'Убедитесь, что POST-запрос с некорректными данными, '
            f'отправленный к`{self.url}`, возвращает ответ со статусом 401'
        )

    def test_jwt_create_with_empty_field(self, user, guest):
        invalid_data = (
            {
                'email': '',
                'password': user.password
            },
            {
                'email': user.email,
                'password': ''
            },
        )
        for data in invalid_data:
            response = guest.post(self.url, data=data)
            assert response.status_code == HTTPStatus.BAD_REQUEST, (
                'Убедитесь, что POST-запрос с некорректными данными, '
                f'отправленный к`{self.url}`, возвращает ответ со статусом 400'
            )
