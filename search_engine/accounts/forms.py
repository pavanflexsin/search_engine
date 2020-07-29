from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms import BooleanField, ValidationError


from accounts.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserAuthenticationForm(AuthenticationForm):

    def clean(self):
        username = self.cleaned_data.get('username')
        return super().clean()

    def confirm_login_allowed(self, user):
        if user.is_superuser is True:
            raise ValidationError("Permession Denied", code="access_denied")
        return super().confirm_login_allowed(user)