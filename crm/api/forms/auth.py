from django import forms

class SineUpForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"size": "40"}), max_length=40, required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"size": "40"}), max_length=40, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
