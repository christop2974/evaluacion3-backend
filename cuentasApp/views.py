from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.decorators.http import require_POST
from propiedadesApp.models import Propiedad, SolicitudVisita
from asesoriaApp.models import Consejo
from .forms import UsuarioCrearForm
from .decorators import perfil_requerido, perfil_usuario


def iniciar_sesion(request):
    if request.user.is_authenticated: return redirect('dashboard')
    form = AuthenticationForm(request, data=request.POST or None)
    form.fields['username'].widget.attrs.update({'class': 'form-control', 'autocomplete': 'username'})
    form.fields['password'].widget.attrs.update({'class': 'form-control', 'autocomplete': 'current-password'})
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        messages.success(request, 'Sesión iniciada correctamente.')
        return redirect('dashboard')
    return render(request, 'cuentas/login.html', {'form': form})

@login_required
def dashboard(request):
    rol = perfil_usuario(request.user)
    context = {'rol': rol, 'total_propiedades': Propiedad.objects.count(), 'total_consejos': Consejo.objects.count(), 'total_visitas': SolicitudVisita.objects.count(), 'ultimas_visitas': SolicitudVisita.objects.select_related('propiedad')[:5]}
    if rol == 'Administrador': context['total_usuarios'] = User.objects.count()
    return render(request, 'cuentas/dashboard.html', context)

@perfil_requerido('Administrador')
def usuarios(request):
    q = request.GET.get('q','').strip()
    lista = User.objects.prefetch_related('groups').order_by('username')
    if q: lista = lista.filter(Q(username__icontains=q)|Q(email__icontains=q)|Q(first_name__icontains=q)|Q(last_name__icontains=q))
    return render(request, 'cuentas/usuarios.html', {'usuarios':lista, 'perfil_usuario':perfil_usuario})

@perfil_requerido('Administrador')
def usuario_nuevo(request):
    form = UsuarioCrearForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        group, _ = Group.objects.get_or_create(name=form.cleaned_data['perfil'])
        user.groups.add(group)
        user.is_staff = (group.name == 'Administrador')
        user.save(update_fields=['is_staff'])
        messages.success(request, f'Usuario {user.username} creado con perfil {group.name}.')
        return redirect('usuarios')
    return render(request, 'cuentas/usuario_form.html', {'form':form, 'titulo':'Crear usuario'})

@perfil_requerido('Administrador')
@require_POST
def usuario_eliminar(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user == request.user or user.is_superuser:
        messages.error(request, 'No puedes eliminar tu propio usuario ni un superusuario.')
    else:
        user.delete(); messages.success(request, 'Usuario eliminado.')
    return redirect('usuarios')

def acceso_denegado(request, exception=None):
    return render(request, 'cuentas/403.html', status=403)
