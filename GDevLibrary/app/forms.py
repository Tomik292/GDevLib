from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import Message, Article, UserExtension

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField();

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['re_password']
        email = self.cleaned_data['email']

        if len(password) < 8:
            raise forms.ValidationError("Password needs to be atleast 8 characters long!")

        if password != re_password:
            raise forms.ValidationError("Passwords aren't matching!")

class UserExtensionForm(forms.ModelForm):

    class Meta:
        model = UserExtension
        fields = ['picture','bio','location']

class LoginForm(forms.Form):
    name = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['recipient', 'subject' ,'text']

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['name','picture','engine','text','tags']