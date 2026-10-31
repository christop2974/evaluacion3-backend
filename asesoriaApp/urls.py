from django.urls import path
from . import views
urlpatterns = [
    path('', views.asesoria, name='asesoria'),
    path('consejos/', views.consejos, name='consejos'),
    path('gestion/consejos/', views.consejos_gestion, name='consejos_gestion'),
    path('gestion/consejos/nuevo/', views.consejo_nuevo, name='consejo_nuevo'),
    path('gestion/consejos/<int:pk>/editar/', views.consejo_editar, name='consejo_editar'),
    path('gestion/consejos/<int:pk>/eliminar/', views.consejo_eliminar, name='consejo_eliminar'),
]
