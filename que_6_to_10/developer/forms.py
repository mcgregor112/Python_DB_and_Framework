from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
