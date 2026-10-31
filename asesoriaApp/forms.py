from django import forms
from .models import Consejo

class ConsejoForm(forms.ModelForm):
    class Meta:
        model = Consejo
        fields = ['titulo', 'descripcion', 'activo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
