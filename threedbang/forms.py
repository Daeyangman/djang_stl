from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import StlFile


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required= True)
    class Meta:
        model = User
        fields = ("username" , 'email' , 'password1',)
    def save(self, commit =True):
        user = super(CreateUserForm, self).save(commit = False)
        user.email = self.cleanded_data["email"]
        if commit:
             user.save()
        return user

class UploadForm(forms.ModelForm):
    class Meta:
        model = StlFile
        fields = ('file',)