from django import forms

class DFAForm(forms.Form):
    testStrings = forms.CharField(widget=forms.Textarea(attrs={'name':'testStrings', 'rows':'10', 'cols':'100', 'placeholder': 'Patterns accepted are ICMBS, ICITS, ICIRPEBS, ICBAES, ICBMSS, ICEABT, ICEFR, ICCSNS, ICCSPEE, ICCSIEE, ICCBEE, ICAASS, ICAPM, ICAIMLBDE, ICAIRME, EUICNB, EUIC3BCB, EUIWNMC, EUCELS', 'style': 'border-radius: 1em;'}))