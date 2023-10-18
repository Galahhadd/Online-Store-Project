from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = CustomUser
		fields = ['email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2']
		widgets = {
				'email': forms.EmailInput(),
				'first_name': forms.TextInput(),
				'last_name': forms.TextInput(),
				'phone_number': forms.TextInput(),
				'password1': forms.PasswordInput(),
				'password2': forms.PasswordInput()
				}

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ['email', 'first_name', 'last_name', 'phone_number']
		widgets = {
				'email': forms.EmailInput(),
				'first_name': forms.TextInput(),
				'last_name': forms.TextInput(),
				'phone_number': forms.TextInput()
				}





