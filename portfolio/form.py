from django import forms


class followers_form(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField(max_length=35)








