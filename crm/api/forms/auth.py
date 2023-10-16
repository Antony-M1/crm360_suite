from django import forms
from crm.models import UserAU

class UserForm(forms.ModelForm):
    # Custom field attributes
    first_name = forms.CharField(max_length=10, required=True)
    last_name = forms.CharField(max_length=10, required=True)

    class Meta:
        model = UserAU
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }
