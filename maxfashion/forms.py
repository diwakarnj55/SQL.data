from django import forms
from .models import Jewellery, Checkout
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django .forms import TextInput,FileInput,Select,Textarea

class LoginForm(AuthenticationForm):
    username = UsernameField(label='Enter Username', widget=forms.TextInput(attrs={"type":"text","class":"form-control","aria-describedby":"emailHelp","placeholder":"Enter Username"}))
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={"type":"password","class":"form-control","id":"exampleInputPassword1","placeholder":"Password"}))

class StoreForm(forms.ModelForm):
    class Meta:
        model=Jewellery
        fields =['jel_item','jel_rate','jel_image']
        widgets ={
            'jel_item':TextInput(attrs={
                "type":"text", 
                "class":"form-control", 
                "id":"exampleInputEmail1", 
                "aria-describedby":"emailHelp", 
                "style":"width: 500px;",
            }),
            'jel_rate':TextInput(attrs={
                "type":"text", 
                "class":"form-control", 
                "id":"exampleInputPassword1", 
                "style":"width: 500px;",
            }),
            'jel_image':FileInput(attrs={
                "type":"File", 
                "class":"form-control", 
                "id":"exampleInputEmail1", 
                "aria-describedby":"emailHelp", 
                "style":"width: 500px;",
            }),
        }
class CheckoutForm(forms.ModelForm):
    class Meta:
        model=Checkout
        fields =['Firstname','Lastname','Emailaddress','phonenumber','Addressline1','Addressline2','country','region']
        widgets ={
            'Firstname':TextInput(attrs={
                "type":"text", 
                "class":"form-control", 
                "placeholder":"First name", 
                "aria-label":"First name",
            }),
            'Lastname':TextInput(attrs={
                "type":"text", 
                "class":"form-control", 
                "placeholder":"Last name", 
                "aria-label":"Last name",
            }),
            'Emailaddress':TextInput(attrs={
                "type":"text", 
                "class":"form-control", 
                "placeholder":"Email Address", 
                "aria-label":"Email Address",
            }),
            'phonenumber':TextInput(attrs={
                "type":"phone", 
                "class":"form-control", 
                "placeholder":"phone Number", 
                "aria-label":"phone Number",
            }),
            'Addressline1':Textarea(attrs={
                "type":"Textarea", 
                "class":"form-control", 
                "placeholder":"Address Line 1", 
                "aria-label":"Address Line1",
                "style":"width: 500px;",
                "style":"height: 200px;",
            }),
            'Addressline2':Textarea(attrs={
                "type":"Textarea", 
                "class":"form-control", 
                "placeholder":"Address Line 2", 
                "aria-label":"Address Line 2",
                "style":"width: 500px;",
                "style":"height: 200px;",
            }),
            'country':Select(attrs={
                "type":"Select", 
                "class":"form-control", 
                "placeholder":"country", 
                "aria-label":"country",
            }),
            'region':Select(attrs={
                "type":"select", 
                "class":"form-control", 
                "placeholder":"region", 
                "aria-label":"region",
            }),
        }

