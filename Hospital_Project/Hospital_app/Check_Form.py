from django import forms


class CheckForm(forms.Form):
    unique_id = forms.CharField(label='UniqueID')
