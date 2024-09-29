from django import forms

class SForm(forms.Form):
    roll = forms.CharField(max_length =10)