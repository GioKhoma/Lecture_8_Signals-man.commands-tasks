import pytest
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

@pytest.mark.django_db
def test_password_reset_sends_email(client, django_user_model, mailoutbox):
    user = django_user_model.objects.create_user(email="reset@test.com", password="123")
    response = client.post(reverse("users:password_reset"), {"email": "reset@test.com"})

    reset_emails = [m for m in mailoutbox if "Reset Your Password" in m.subject]
    assert len(reset_emails) == 1, f"Subjects sent: {[m.subject for m in mailoutbox]}"


@pytest.mark.django_db
def test_password_reset_confirm_valid_token(client, django_user_model):
    user = django_user_model.objects.create_user(email="tok@test.com", password="old")
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    response = client.post(reverse("users:custom_password_reset_confirm", kwargs={"uidb64": uid, "token": token}), {
        "new_password1": "NewStrongPass123!",
        "new_password2": "NewStrongPass123!",
    })
    assert response.status_code == 302
