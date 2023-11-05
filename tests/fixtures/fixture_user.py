import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        email='user@example.com',
        password='user1password',
    )


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create_user(
        email='author@example.com',
        password='author1password',
    )


@pytest.fixture
def admin(django_user_model):
    return django_user_model.objects.create_superuser(
        email='admin@example.com',
        password='admin1password',
    )


@pytest.fixture
def token_user(user):
    token = AccessToken.for_user(user)
    return {
        'access': str(token),
    }


@pytest.fixture
def user_client(token_user):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'JWT {token_user["access"]}')
    return client


@pytest.fixture
def token_author(author):
    token = AccessToken.for_user(author)
    return {
        'access': str(token),
    }


@pytest.fixture
def author_client(token_author):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'JWT {token_author["access"]}')
    return client


@pytest.fixture
def token_admin(admin):
    token = AccessToken.for_user(admin)
    return {
        'access': str(token),
    }


@pytest.fixture
def admin_client(token_admin):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'JWT {token_admin["access"]}')
    return client


@pytest.fixture
def guest():
    return APIClient()
