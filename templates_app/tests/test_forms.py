import pytest
from templates_app.forms import ContactForm

def test_invalid_contact_form():
    form = ContactForm(data={"name": "", "email": "notemail", "message": ""})
    assert not form.is_valid()
