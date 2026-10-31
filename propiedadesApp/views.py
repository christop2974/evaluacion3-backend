from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PropiedadForm, SolicitudVisitaForm
from .models import Propiedad, SolicitudVisita
from cuentasApp.decorators import perfil_requerido


def inicio(request):
    destacadas = Propiedad.objects.filter(destacada=True)[:3]
    if not destacadas.exists():
        destacadas = Propiedad.objects.all()[:3]
    return render(request, 'propiedades/inicio.html', {
        'destacadas': destacadas,
        'total': Propiedad.objects.count(),
    })


def propiedades(request):
    qs = Propiedad.objects.all()
    q = request.GET.get('q', '').strip()
    tipo = request.GET.get('tipo', '').strip()
    comuna = request.GET.get('comuna', '').strip()
    operacion = request.GET.get('operacion', '').strip()

    if q:
        qs = qs.filter(Q(titulo__icontains=q) | Q(comuna__icontains=q) | Q(sector__icontains=q) | Q(descripcion__icontains=q))
    if tipo:
        qs = qs.filter(tipo=tipo)
    if comuna:
        qs = qs.filter(comuna__icontains=comuna)
    if operacion:
        qs = qs.filter(operacion=operacion)

    return render(request, 'propiedades/listado.html', {
        'propiedades': qs,
        'tipos': Propiedad.TIPO_CHOICES,
        'operaciones': Propiedad.OPERACION_CHOICES,
    })


def detalle(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        form = SolicitudVisitaForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.propiedad = propiedad
            solicitud.save()
            messages.success(request, 'Tu solicitud de visita fue registrada correctamente.')
            return redirect('detalle', pk=pk)
    else:
        form = SolicitudVisitaForm()
    return render(request, 'propiedades/detalle.html', {'propiedad': propiedad, 'form': form})


@perfil_requerido('Administrador', 'Supervisor')
def crear(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Propiedad creada correctamente.')
            return redirect('panel')
    else:
        form = PropiedadForm()
    return render(request, 'propiedades/formulario.html', {'form': form, 'titulo': 'Agregar propiedad'})


@perfil_requerido('Administrador', 'Supervisor')
def editar(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()
            messages.success(request, 'Propiedad modificada correctamente.')
            return redirect('panel')
    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'propiedades/formulario.html', {'form': form, 'titulo': 'Modificar propiedad'})


@perfil_requerido('Administrador')
def eliminar(request, pk):
    propiedad = get_object_or_404(Propiedad, pk=pk)
    if request.method == 'POST':
        propiedad.delete()
        messages.success(request, 'Propiedad eliminada correctamente.')
        return redirect('panel')
    return render(request, 'propiedades/eliminar.html', {'propiedad': propiedad})


@perfil_requerido('Administrador', 'Supervisor', 'Administrativo')
def panel(request):
    propiedades_qs = Propiedad.objects.all()
    q = request.GET.get('q', '').strip()
    if q:
        propiedades_qs = propiedades_qs.filter(Q(titulo__icontains=q) | Q(comuna__icontains=q))
    from cuentasApp.decorators import perfil_usuario
    return render(request, 'propiedades/panel.html', {'propiedades': propiedades_qs, 'rol': perfil_usuario(request.user)})


from django.views.decorators.http import require_POST

@perfil_requerido('Administrador', 'Supervisor', 'Administrativo')
def visitas_gestion(request):
    q = request.GET.get('q', '').strip()
    visitas = SolicitudVisita.objects.select_related('propiedad').all()
    if q:
        visitas = visitas.filter(Q(nombre__icontains=q) | Q(email__icontains=q) | Q(propiedad__titulo__icontains=q))
    return render(request, 'gestion/visitas.html', {'visitas': visitas})

@perfil_requerido('Administrador')
@require_POST
def visita_eliminar(request, pk):
    visita = get_object_or_404(SolicitudVisita, pk=pk)
    visita.delete()
    messages.success(request, 'Solicitud de visita eliminada.')
    return redirect('visitas_gestion')
