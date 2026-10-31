from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('propiedades/', views.propiedades, name='propiedades'),
    path('propiedades/<int:pk>/', views.detalle, name='detalle'),
    path('propiedades/nueva/', views.crear, name='crear'),
    path('propiedades/<int:pk>/editar/', views.editar, name='editar'),
    path('propiedades/<int:pk>/eliminar/', views.eliminar, name='eliminar'),
    path('panel/', views.panel, name='panel'),
    path('gestion/visitas/', views.visitas_gestion, name='visitas_gestion'),
    path('gestion/visitas/<int:pk>/eliminar/', views.visita_eliminar, name='visita_eliminar'),
]
