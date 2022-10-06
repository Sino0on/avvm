from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .widget import *
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField
    year = forms.DateField
    image = forms.ImageField
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          'class': 'form-control'
                                          }),
    )
    password2 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          'class': 'form-control'
                                          }),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'age', 'first_name', 'last_name', 'image', 'profession']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
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
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'date': forms.DateField(),
            'is_prior': forms.CheckboxInput(attrs={'class': 'form-check-input mt-0',
                                                   'aria-label': 'Checkbox for following text input',
                                                   'style': 'float: left;margin-left: 0;'
                                                   })
        }


class EventCreateForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    category = forms.Select(attrs={'class': 'form-select'})

    class Meta:
        model = Events
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'preview': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
