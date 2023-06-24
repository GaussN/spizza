from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from catalog.models import Pizza


class CreateUser(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    last_name = forms.CharField(label='Фамилия',
                                  widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class LoginUser(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ('name', 'description', 'price', 'image', 'pizza_type', 'dough_type', 'size')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': '3'}),
            'price': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'image': forms.FileInput(attrs={'class': 'form-control mb-3'}),
            'pizza_type': forms.Select(attrs={'class': 'form-control mb-3'}),
            'dough_type': forms.Select(attrs={'class': 'form-control mb-3'}),
            'size': forms.Select(attrs={'class': 'form-control mb-3'}),
        }
