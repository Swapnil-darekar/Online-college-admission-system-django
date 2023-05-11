from django import forms
from .models import Application
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('user', 'Application_Status', 'message',)


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
