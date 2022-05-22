from django import forms

class DFAForm(forms.Form):
    testStringsField = forms.CharField(widget=forms.Textarea(attrs={'name':'testStrings', 'rows':'10', 'cols':'100'}))