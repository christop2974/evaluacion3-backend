import json
from pathlib import Path
from django.core.management.base import BaseCommand
from propiedadesApp.models import Propiedad


class Command(BaseCommand):
    help = 'Carga las propiedades iniciales desde el JSON heredado del proyecto.'

    def handle(self, *args, **options):
        ruta = Path(__file__).resolve().parents[3] / 'data' / 'propiedades.json'
        if not ruta.exists():
            self.stderr.write(self.style.ERROR(f'No se encontró {ruta}'))
            return
        datos = json.loads(ruta.read_text(encoding='utf-8'))
        creadas = 0
        for item in datos:
            _, created = Propiedad.objects.update_or_create(
                id=item['id'],
                defaults={
                    'titulo': item['nombre'],
                    'tipo': item['tipo'] if item['tipo'] in dict(Propiedad.TIPO_CHOICES) else 'Casa',
                    'operacion': 'Venta',
                    'comuna': item['comuna'],
                    'sector': '',
                    'precio': int(str(item['precio']).replace('$', '').replace('.', '').replace(',', '')),
                    'dormitorios': item.get('habitaciones', 0),
                    'banos': item.get('banos', 0),
                    'superficie': 0,
                    'descripcion': f"{item['nombre']} ubicada en {item['comuna']}.",
                    'imagen': item.get('imagen', ''),
                    'destacada': item.get('destacada', False),
                },
            )
            creadas += int(created)
        self.stdout.write(self.style.SUCCESS(f'Propiedades procesadas: {len(datos)}. Nuevas: {creadas}.'))
