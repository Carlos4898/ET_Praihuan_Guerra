from django import forms
from django.forms import ModelForm 
from django.forms import widgets #permite definir la configuración de los datos de entrada del form
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Gato, Cliente

class GatoForm(forms.ModelForm):
    
    class Meta: #permite configurar el form 
        model = Gato 
        fields = ['chip', 'nombre', 'raza', 'categoria', 'imagen']
        labels = {
            'chip': 'Chip',
            'nombre': 'Nombre',
            'raza': 'Raza',
            'categoria': 'Categoria',
            'imagen': 'Imagen'
        }
        widgets={
            'chip': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite el n° de chip',
                    'id': 'chip'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Escriba el nombre',
                    'id': 'nombre'
                }
            ),
            'raza': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Raza de gato',
                    'id': 'raza'
                }
            ),
            'categoria':forms.Select(
                attrs = {
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen',
                }
            )
        }

class ClienteForm(forms.ModelForm):
    
    class Meta: #permite configurar el form 
        model = Cliente 
        fields = ['rut', 'nombre', 'numero']
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'numero': 'Numero',
        }
        widgets={
            'rut': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite su rut',
                    'id': 'rut'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Escriba su nombre',
                    'id': 'nombre'
                }
            ),
            'numero': forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder': 'Escriba su número',
                    'id': 'numero'
                }
            ),
        }
