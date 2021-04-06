from django import forms
from .models import Userinfo


class RegForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput())
    Confirm_Password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Userinfo
        fields = "__all__"



