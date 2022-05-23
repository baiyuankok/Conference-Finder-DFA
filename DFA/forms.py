from django import forms

class DFAForm(forms.Form):
    testStrings = forms.CharField(widget=forms.Textarea(attrs={'name':'testStrings', 'rows':'10', 'cols':'100', 'placeholder': 'Insert text here...', 'style': 'border-radius: 1em;'}))