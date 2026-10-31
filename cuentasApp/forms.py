from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UsuarioCrearForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña temporal', widget=forms.PasswordInput(attrs={'class':'form-control'}), validators=[validate_password])
    perfil = forms.ChoiceField(label='Perfil', choices=[('Administrador','Administrador'),('Supervisor','Supervisor'),('Administrativo','Administrativo')], widget=forms.Select(attrs={'class':'form-select'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {k: forms.TextInput(attrs={'class':'form-control'}) for k in ['username','first_name','last_name']}
        widgets['email'] = forms.EmailInput(attrs={'class':'form-control'})
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit: user.save()
        return user
