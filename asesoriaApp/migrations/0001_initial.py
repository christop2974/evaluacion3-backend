from django.db import migrations, models


def cargar_consejos(apps, schema_editor):
    Consejo = apps.get_model('asesoriaApp', 'Consejo')
    datos = [
        ('Define tu presupuesto', 'Antes de buscar una propiedad, calcula cuánto puedes invertir y considera gastos adicionales.'),
        ('Revisa la ubicación', 'Evalúa conectividad, servicios, seguridad y cercanía a los lugares importantes para ti.'),
        ('Visita la propiedad', 'Observa el estado general y resuelve tus dudas antes de tomar una decisión.'),
        ('Compara alternativas', 'Revisa varias propiedades para identificar la opción que mejor se adapta a tus necesidades.'),
    ]
    Consejo.objects.bulk_create([Consejo(titulo=t, descripcion=d) for t, d in datos])


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Consejo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['titulo'], 'verbose_name': 'Consejo', 'verbose_name_plural': 'Consejos'},
        ),
        migrations.RunPython(cargar_consejos, migrations.RunPython.noop),
    ]
