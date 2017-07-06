from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Please enter your ID'
            }
        ),
        max_length=24,
    )

    nickname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nickname should be unique'
            }
        )
    )
    mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Phonenumber ex)01012345678',
                'required': 'true'
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Please enter your password'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm your password'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username already exists'
            )
        return username

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if nickname and User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError(
                'Nickname already exists'
            )
        return nickname

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'Not valid password'
            )
        return password2

    def create_user(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password2']
        nickname = self.cleaned_data['nickname']

        user = User.objects.create_user(
            username=username,
            password=password,
            nickname=nickname
        )
        return user