from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .widget import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    year = forms.DateField
    image = forms.ImageField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age', 'first_name', 'last_name', 'image', 'profession']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),

        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'exampleInputPassword1'})
        }


class NewsCreateForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'preview': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(),
            'date': forms.DateField()
        }


class EventCreateForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    start = forms.DateTimeField(widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M'))

    class Meta:
        model = Events
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'preview': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-label', 'for': 'formFile'}),
            'date': forms.DateField(),
            'start':  forms.TextInput(attrs={'class': 'vDateField'})
        }
