import pytest
from django.urls import reverse
from templates_app.models import Contact, Employee


@pytest.mark.django_db
def test_home_view_logged_in(client, django_user_model):
    user = django_user_model.objects.create_user(email="test@test.com", password="123")
    client.login(email="test@test.com", password="123")
    response = client.get(reverse("templates_app:home"))
    assert response.status_code == 200
    assert "Welcome Back" in response.content.decode()


@pytest.mark.django_db
def test_contact_form_submission(client, django_user_model):
    user = django_user_model.objects.create_user(email="test@test.com", password="123")
    client.login(email="test@test.com", password="123")
    data = {"name": "Gio", "email": "gio@mail.scsa", "message": "hello"}
    response = client.post(reverse("templates_app:contact"), data)
    assert Contact.objects.filter(email="gio@mail.scsa").exists()

@pytest.mark.django_db
def test_employee_creation(client, django_user_model):
    user = django_user_model.objects.create_user(email="hr@test.com", password="123")
    client.login(email="hr@test.com", password="123")
    response = client.post(reverse("templates_app:employee"), {
        "first_name": "Lasha",
        "last_name": "Kutalia",
        "email": "lasha@example.com",
    })
    assert Employee.objects.filter(first_name="Lasha").exists()

