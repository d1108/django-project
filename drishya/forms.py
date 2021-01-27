from django import forms
from drishya.models import images2,register,Profile
# from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class picture(forms.ModelForm):
    class Meta:
        model = images2
        fields = ['img','caption','price']

class reg(forms.ModelForm):
    class Meta:
        model = register
        fields = ['first_name','last_name','email','password','mobile_no','img']
        widgets = {
        'password': forms.PasswordInput(),
    }
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mobile_no','img']
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

