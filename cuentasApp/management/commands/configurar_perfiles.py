from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from propiedadesApp.models import Propiedad, SolicitudVisita
from asesoriaApp.models import Consejo

class Command(BaseCommand):
    help = 'Crea grupos y permisos base para los perfiles PNK.'
    def handle(self, *args, **options):
        modelos = [Propiedad, SolicitudVisita, Consejo]
        permisos = {}
        for modelo in modelos:
            ct = ContentType.objects.get_for_model(modelo)
            permisos[modelo.__name__] = list(Permission.objects.filter(content_type=ct))
        admin, _ = Group.objects.get_or_create(name='Administrador')
        supervisor, _ = Group.objects.get_or_create(name='Supervisor')
        administrativo, _ = Group.objects.get_or_create(name='Administrativo')
        admin.permissions.set(Permission.objects.all())
        supervisor.permissions.set([p for modelo in ('Propiedad','Consejo','SolicitudVisita') for p in permisos[modelo] if p.codename.startswith(('view_','add_','change_'))])
        administrativo.permissions.set([p for modelo in ('Propiedad','Consejo','SolicitudVisita') for p in permisos[modelo] if p.codename.startswith('view_')] + [p for p in permisos['SolicitudVisita'] if p.codename.startswith('add_')])
        self.stdout.write(self.style.SUCCESS('Perfiles configurados: Administrador, Supervisor y Administrativo.'))
