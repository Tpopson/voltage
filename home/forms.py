from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from . models import *
from userprofile.models import *
from shopcart.models import *


class ContactForm(forms.ModelForm):
    class Meta:
       model = Contact
       fields = ['full_name','email','message']



class SignupForm(UserCreationForm):
    username = forms.CharField(max_length= 50)
    first_name = forms.CharField(max_length= 100)
    last_name = forms.CharField(max_length= 100)
    email = forms.EmailField(max_length= 150)

    
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')





STATE = [ 
    ('Abia','Abia'),
    ('Delta','Delta'),
    ('Edo','Edo'),
    ('Imo','Imo'),
    ('Lagos','Lagos'),
    ('Ogun','Ogun'),
    ('Ondo','Ondo'),
]
class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['first_name','last_name','phone','address','state','pix']
        widgets ={
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':' Home Address'}),
            'state':forms.Select(attrs={'class':'form-control', 'placeholder':'State'}, choices=STATE),
            'pix':forms.FileInput(attrs={'class':'form-control'})
        }



class ShopcartForm(forms.ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


        
class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Old Password'}))
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter New Password'}))
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter repeat new Password'}))

    class Meta:
        model = User 
        fields = ('old_password','new_password1','new_password2')


    def __init__(self,*args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'