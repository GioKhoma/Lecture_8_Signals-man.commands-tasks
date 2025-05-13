import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_login_success(client, django_user_model):
    user = django_user_model.objects.create_user(email="user@test.com", password="123")
    response = client.post(reverse("users:login_user"), {
        "username": "user@test.com", "password": "123"
    })
    assert response.status_code == 302  # Redirect to home

@pytest.mark.django_db
def test_logout(client, django_user_model):
    user = django_user_model.objects.create_user(email="log@test.com", password="123")
    client.login(email="log@test.com", password="123")
    response = client.get(reverse("users:logout_user"))
    assert response.status_code == 302
