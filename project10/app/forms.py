from django import forms 
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        Model = User 
        field = ['first_name','last_name','email','username','password']
        weidth = {'password':forms.PasswordInput}
        help_text = {'username':''}

class Profileform(forms.ModelForm):
    class Meta:
        Model = Profile
        exclude =['username']

