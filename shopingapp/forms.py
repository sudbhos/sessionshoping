from django import forms

class addi(forms.Form):

    name=forms.CharField()
    quentity=forms.IntegerField()

