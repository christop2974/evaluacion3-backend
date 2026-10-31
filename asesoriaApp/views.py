from django.shortcuts import render
from .models import Consejo
from .forms import ConsejoForm
from cuentasApp.decorators import perfil_requerido
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST


def asesoria(request):
    servicios = [
        'Compra de propiedades',
        'Venta de propiedades',
        'Orientación para arriendo',
        'Evaluación de alternativas',
    ]
    return render(request, 'asesoriaApp/asesoria.html', {'servicios': servicios})


def consejos(request):
    return render(request, 'asesoriaApp/consejos.html', {'consejos': Consejo.objects.filter(activo=True)})


@perfil_requerido('Administrador', 'Supervisor', 'Administrativo')
def consejos_gestion(request):
    q = request.GET.get('q', '').strip()
    lista = Consejo.objects.all()
    if q: lista = lista.filter(Q(titulo__icontains=q) | Q(descripcion__icontains=q))
    from cuentasApp.decorators import perfil_usuario
    return render(request, 'gestion/consejos.html', {'consejos': lista, 'rol': perfil_usuario(request.user)})

@perfil_requerido('Administrador', 'Supervisor')
def consejo_nuevo(request):
    form = ConsejoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(); messages.success(request, 'Consejo creado correctamente.'); return redirect('consejos_gestion')
    return render(request, 'gestion/consejo_form.html', {'form': form, 'titulo': 'Crear consejo'})

@perfil_requerido('Administrador', 'Supervisor')
def consejo_editar(request, pk):
    consejo = get_object_or_404(Consejo, pk=pk)
    form = ConsejoForm(request.POST or None, instance=consejo)
    if request.method == 'POST' and form.is_valid():
        form.save(); messages.success(request, 'Consejo actualizado correctamente.'); return redirect('consejos_gestion')
    return render(request, 'gestion/consejo_form.html', {'form': form, 'titulo': 'Editar consejo'})

@perfil_requerido('Administrador')
@require_POST
def consejo_eliminar(request, pk):
    get_object_or_404(Consejo, pk=pk).delete(); messages.success(request, 'Consejo eliminado.'); return redirect('consejos_gestion')
