from django import forms
from django.forms import ModelForm
from TODO_LIST_APP.models import Task
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title ( max. 255 characters )', 'maxlength': 255}))

    class Meta:
        model = Task
        fields =[ 'title']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Mật khẩu không khớp!")


    