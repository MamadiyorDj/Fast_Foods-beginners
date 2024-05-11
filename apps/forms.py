from django import forms
from .models import Users
from phonenumber_field.formfields import PhoneNumberField


class UserForm(forms.Form):
    phone_number = PhoneNumberField(required=False)