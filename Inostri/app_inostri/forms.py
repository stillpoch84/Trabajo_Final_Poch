from django import forms

class VinoFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64) 
    bodega = forms.CharField(required=True, max_length=64)
    varietal = forms.CharField(required=True, max_length=64)
    cosecha = forms.IntegerField(required=True)
    region = forms.CharField(required=True, max_length=64)
    provincia = forms.CharField(required=True, max_length=64) 