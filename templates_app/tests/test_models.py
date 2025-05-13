import pytest
from templates_app.models import Profile, Contact


@pytest.mark.django_db
def test_profile_str_representation():
    profile = Profile.objects.create(full_name="Ana Dolidze")
    assert str(profile) == "Ana Dolidze"

@pytest.mark.django_db
def test_contact_str():
    contact = Contact.objects.create(name="Nika", email="nika@test.scsa", message="Hello")
    assert "Message from Nika" in str(contact)