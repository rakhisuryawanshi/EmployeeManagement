from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import EmployeeManagement

class myloginform(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label='Password',
    strip=False,
    widget=forms.PasswordInput(attrs={'autocomplate':'current-password','class':'form-control'}))

class signupform(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Retype Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','email')
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}

class MyChangePasswordForm(PasswordChangeForm):
     old_password=forms.CharField(label="old password"),
     strip=False,
     widget=forms.PasswordInput(attrs={'autocomplete':'current_password',
     'autofocus':True,'class':'form-control'})

     new_password1=forms.CharField(label="New Password 1"),
     strip=False,
     widget=forms.PasswordInput(attrs={'autocomplete':'new_password1',
     'autofocus':True,'class':'form-control'}) 

class Addemployeeform(forms.ModelForm):
    class Meta:
        model=EmployeeManagement
        fields=('First_name','last_name','EmailId','Mobile','Address','Blood_Group')