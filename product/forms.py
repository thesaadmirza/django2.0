from django import forms

class ProductForms(forms.Form):
    title = forms.CharField(max_length=100,attrs={'class':'form-control'})
    price = forms.DecimalField(max_digits=5,decimal_places=3)
    description = forms.CharField(widget=forms.Textarea)
