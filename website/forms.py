from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(Label="", wiget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email-Address'}))
    first_name = forms.CharField(Label="",max_length=100, wiget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(Label="",max_length=100, wiget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last-Name'}))

    class Meta:
        model = User
        fields = {'username','first_name','last_name','email','password1','password2'}

    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)

        self.fields['username'].widget_attrs['class'] = 'form-control'
        self.fields['username'].widget_attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class = "form-text text-muted small"><ul><li>Your password cannot be too similar to your other personal information</li><li>Your password must contains at least 8 characters</li></ul>'

        self.fields['password1'].widget_attrs['class'] = 'form-control'
        self.fields['password1'].widget_attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        #self.fields['password1'].help_text = '<span class = "form-text text-muted small"><ul><li>Your password cannot be too similar to your other personal information</li><li>Your password must contains at least 8 characters</li></ul>'

        self.fields['password2'].widget_attrs['class'] = 'form-control'
        self.fields['password2'].widget_attrs['placeholder'] = 'User Name'
        self.fields['password2'].label = ''
        #self.fields['password2'].help_text = '<span class = "form-text text-muted small"><ul><li>Your password cannot be too similar to your other personal information</li><li>Your password must contains at least 8 characters</li></ul>'

