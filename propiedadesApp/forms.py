from django import forms
from .models import Propiedad, SolicitudVisita


class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = [
            'titulo', 'tipo', 'operacion', 'comuna', 'sector', 'precio',
            'dormitorios', 'banos', 'superficie', 'descripcion', 'imagen', 'destacada'
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Departamento moderno con vista al mar'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'operacion': forms.Select(attrs={'class': 'form-select'}),
            'comuna': forms.TextInput(attrs={'class': 'form-control'}),
            'sector': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'dormitorios': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'banos': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'superficie': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': '0.01'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'imagen': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'img/departamento.png'}),
            'destacada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class SolicitudVisitaForm(forms.ModelForm):
    class Meta:
        model = SolicitudVisita
        fields = ['nombre', 'email', 'telefono', 'fecha_preferida', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.cl'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56 9 1234 5678'}),
            'fecha_preferida': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Horario o información adicional'}),
        }
