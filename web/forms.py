from django import forms
from .models import Productos, Contactos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'imagen','privado']
        labels = {
            'nombre':'Nombre del producto:',
            'descripcion': 'Descripción del producto:',
            'imagen':'Imagen del producto:',
            'privado':'Privacidad:'
        }

#Esta versión creará un modelo utilizando forms.Form
# from django import forms

# class ProductoForm(forms.Form):
#     nombre = forms.CharField(max_length=64, required=True)
#     descripcion = forms.CharField(widget=forms.Textarea, required=True)
#     imagen = forms.ImageField(required=True)
#     privado = forms.ChoiceField(choices=[(True, 'Privado'), (False, 'Público')], required=True)

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = ['NombreCliente','EmailCliente', 'Mensaje']
        labels = {
            'NombreCliente': 'Su nombre:',
            'EmailCliente':'Correo electrónico:',
            'Mensaje':'Motivo de su contacto:'
        }