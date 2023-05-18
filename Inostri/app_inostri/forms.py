from django import forms

# class VinoFormulario(forms.Form):
#     nombre = forms.CharField(required=True, max_length=64) 
#     bodega = forms.CharField(required=True, max_length=64)
#     varietal = forms.CharField(required=True, max_length=64)
#     cosecha = forms.IntegerField(required=True, max_value=3000)
#     zona = forms.CharField(required=True, max_length=64)
#     provincia = forms.CharField(required=True, max_length=64) 

# class BodegaFormulario(forms.Form):
#     nombre = forms.CharField(required=True, max_length=64) 
#     direccion = forms.CharField(required=True, max_length=256)
#     zona = forms.CharField(required=True, max_length=64)
#     provincia = forms.CharField(required=True, max_length=64)
#     telefono = forms.CharField(required=False, max_length=20)
#     email = forms.EmailField(required=False) 

# class VarietalFormulario(forms.Form):
#     nombre = forms.CharField(required=True, max_length=64) 
#     descripcion = forms.CharField(required=True, max_length=800) 
