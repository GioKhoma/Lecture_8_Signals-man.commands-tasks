import pytest
from django.urls import reverse
from users.models import CustomUser

@pytest.mark.django_db
def test_register_user(client):
    response = client.post(reverse("users:register_user"), {
        "email": "new@test.com",
        "first_name": "New",
        "last_name": "User",
        "password1": "StrongPass123!",
        "password2": "StrongPass123!"
    })
    assert CustomUser.objects.filter(email="new@test.com").exists()
