from django import forms
from .models import User


class Userform(forms.ModelForm):
    password = forms.CharField(
        widget=(forms.PasswordInput()))  # you can create any custom field other then mentioned in model
    confirm_password = forms.CharField(widget=(forms.PasswordInput()))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'phone_number']

    def clean(self):
        cleaned_data = super(Userform, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Password does not match!')
