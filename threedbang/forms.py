from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import StlFile


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username" , 'password1',)
    def save(self, commit =True):
        user = super(CreateUserForm, self).save(commit = False)
        if commit:
             user.save()
        return user
#
class UploadForm(forms.ModelForm):
    class Meta:
        model = StlFile
        fields = ('file',)