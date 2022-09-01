from django.forms import ModelForm
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class TodoForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task']



class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
