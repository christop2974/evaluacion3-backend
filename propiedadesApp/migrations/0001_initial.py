from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('tipo', models.CharField(choices=[('Casa', 'Casa'), ('Departamento', 'Departamento'), ('Parcela', 'Parcela'), ('Oficina', 'Oficina'), ('Terreno', 'Terreno')], max_length=30)),
                ('operacion', models.CharField(choices=[('Venta', 'Venta'), ('Arriendo', 'Arriendo')], default='Venta', max_length=20)),
                ('comuna', models.CharField(max_length=80)),
                ('sector', models.CharField(blank=True, max_length=100)),
                ('precio', models.DecimalField(decimal_places=0, max_digits=14)),
                ('dormitorios', models.PositiveIntegerField(default=0)),
                ('banos', models.PositiveIntegerField(default=0)),
                ('superficie', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('descripcion', models.TextField(blank=True)),
                ('imagen', models.CharField(blank=True, help_text='Ruta de imagen dentro de static/img/', max_length=255)),
                ('destacada', models.BooleanField(default=False)),
                ('creada', models.DateTimeField(auto_now_add=True)),
                ('actualizada', models.DateTimeField(auto_now=True)),
            ],
            options={'ordering': ['-destacada', '-creada'], 'verbose_name': 'Propiedad', 'verbose_name_plural': 'Propiedades'},
        ),
        migrations.CreateModel(
            name='SolicitudVisita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=30)),
                ('fecha_preferida', models.DateField(blank=True, null=True)),
                ('mensaje', models.TextField(blank=True)),
                ('creada', models.DateTimeField(auto_now_add=True)),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to='propiedadesApp.propiedad')),
            ],
            options={'ordering': ['-creada'], 'verbose_name': 'Solicitud de visita', 'verbose_name_plural': 'Solicitudes de visita'},
        ),
    ]
