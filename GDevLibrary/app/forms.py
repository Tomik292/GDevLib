from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.html import strip_tags

from .models import Message, Article, UserExtension, Comment, SubComment

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

class UserExtensionForm(forms.Form):

    username = forms.CharField(max_length=150, required=False)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    email =  forms.EmailField(required=False)
    bio = forms.CharField(widget=forms.Textarea, max_length=500, required=False)
    location = forms.CharField(max_length=50, required=False)

    def clean(self):
        username = strip_tags(self.cleaned_data['username'])
        first_name =  strip_tags(self.cleaned_data['first_name'])
        last_name = self.cleaned_data['last_name']
        email =  strip_tags(self.cleaned_data['email'])
        bio =  strip_tags(self.cleaned_data['bio'])
        location =  strip_tags(self.cleaned_data['location'])


class ChangePasswordForm(forms.Form):

    new_password = forms.CharField(widget = forms.PasswordInput)
    new_password_again = forms.CharField(widget = forms.PasswordInput)

    def clean(self):
        new_password =  strip_tags(self.cleaned_data['new_password'])
        new_password_again =  strip_tags(self.cleaned_data['new_password_again'])

        if len(new_password) < 8:
            raise forms.ValidationError("Password needs to be atleast 8 characters long!")

        if new_password != new_password_again:
            raise forms.ValidationError("Passwords aren't matching")

class LoginForm(forms.Form):
    name = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        name =  strip_tags(self.cleaned_data['name'])
        password =  strip_tags(self.cleaned_data['password'])

        if not User.objects.filter(username = name).exists():
            raise forms.ValidationError("User doesn't exist!")
        

class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['recipient', 'subject' ,'text']

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['name','picture','engine','text','overview']

class SearchForm(forms.Form):
    key_words = forms.CharField(max_length = 200, label="", widget = forms.TextInput(attrs={'placeholder':'Search'}))

class CommentForm(forms.ModelForm):

    text = forms.CharField(max_length = 500, label = 'Comment:', widget=forms.Textarea, required = False)

    class Meta:
        model = Comment
        fields = ['text']

class SubCommentForm(forms.ModelForm):

    text = forms.CharField(max_length = 500, label = 'Reply:', widget=forms.Textarea(attrs={'rows':2, 'cols':15}), required = False)

    class Meta:

        model = SubComment
        fields = ['text']