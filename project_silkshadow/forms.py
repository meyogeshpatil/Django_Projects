from django import forms

class feedback(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    feedback=forms.CharField()