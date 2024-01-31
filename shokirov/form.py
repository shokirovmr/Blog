from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from shokirov.models import Post


class UserRegistrationModelForm(forms.ModelForm):
    password1 = forms.CharField(max_length=40)
    password2 = forms.CharField(max_length=40)

    def save(self, commit=True):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 == password2:
            user = super().save(commit)
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError("Password is not matching")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class PostCreateForm(forms.ModelForm):
    model = Post
    fields = ["name", "content", "user"]
