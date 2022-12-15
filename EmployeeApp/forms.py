from django import forms
from EmployeeApp.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['emp_id','emp_name','phone','designation','email']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

