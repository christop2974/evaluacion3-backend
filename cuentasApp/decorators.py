from functools import wraps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

ROLES = ('Administrador', 'Supervisor', 'Administrativo')
def perfil_requerido(*perfiles):
    def decorador(view):
        @login_required
        @wraps(view)
        def wrapped(request, *args, **kwargs):
            if request.user.is_superuser or request.user.groups.filter(name='Administrador').exists():
                return view(request, *args, **kwargs)
            if request.user.groups.filter(name__in=perfiles).exists():
                return view(request, *args, **kwargs)
            messages.error(request, 'Tu perfil no tiene permiso para realizar esta operación.')
            return redirect('dashboard')
        return wrapped
    return decorador

def perfil_usuario(user):
    if user.is_superuser or user.groups.filter(name='Administrador').exists(): return 'Administrador'
    for rol in ('Supervisor', 'Administrativo'):
        if user.groups.filter(name=rol).exists(): return rol
    return 'Sin perfil'
