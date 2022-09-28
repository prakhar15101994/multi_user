from accounts.models import MyUser
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import EmailInput, PasswordInput


class RegisterForm(UserCreationForm):
    password1=forms.CharField(label='Password', widget=PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Conferm Password', widget=PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=MyUser
        fields=['username','email', 'first_name','last_name','password1','password2','address', 'city', 'pincode','state', 'patient', 'doctor']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'passord':forms.PasswordInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'patient':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'doctor':forms.CheckboxInput(attrs={'class':'form-check-input'}),
            

        }
class LoginForm(forms.ModelForm):
    class Meta:
        model=MyUser
        fields=['username', 'password']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            # 'password1':forms.PasswordInput(attrs={'class':'form-control'})
        }