from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import StlFile,CustomAddress


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ("username" ,'email', 'password1','password2')
        widgets = {
            'username':forms.TextInput(attrs= {'placeholder' : '아이디'}),

        }
    def save(self, commit =True):
        user = super(CreateUserForm, self).save(commit = False)
        if commit:
             user.save()
        return user
#
class UploadForm(forms.ModelForm):
    class Meta:
        model = StlFile
        fields = ('file', 'comment')
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': '프리프린팅 O,X'}),

        }
        # exclude = ('thumnail_image', 'owner', 'time', 'price',)


class AddressForm(forms.ModelForm):
    class Meta:
        model = CustomAddress
        fields = ('address', 'phone_number','name_user','detail_address')

class TestForm(forms.ModelForm):
    class Meta:
        model = StlFile
        fields =('test_a' ,'test_b')