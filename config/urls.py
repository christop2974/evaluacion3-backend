from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import include, path
from cuentasApp import views as cuenta_views

urlpatterns = [
    path('cuentas/login/', cuenta_views.iniciar_sesion, name='login'),
    path('cuentas/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cuentas/dashboard/', cuenta_views.dashboard, name='dashboard'),
    path('cuentas/usuarios/', cuenta_views.usuarios, name='usuarios'),
    path('cuentas/usuarios/nuevo/', cuenta_views.usuario_nuevo, name='usuario_nuevo'),
    path('cuentas/usuarios/<int:pk>/eliminar/', cuenta_views.usuario_eliminar, name='usuario_eliminar'),
    path('cuentas/password-reset/', auth_views.PasswordResetView.as_view(template_name='cuentas/password_reset.html', email_template_name='cuentas/password_reset_email.html', subject_template_name='cuentas/password_reset_subject.txt', success_url='/cuentas/password-reset/enviado/'), name='password_reset'),
    path('cuentas/password-reset/enviado/', auth_views.PasswordResetDoneView.as_view(template_name='cuentas/password_reset_done.html'), name='password_reset_done'),
    path('cuentas/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='cuentas/password_reset_confirm.html', success_url='/cuentas/reset/completo/'), name='password_reset_confirm'),
    path('cuentas/reset/completo/', auth_views.PasswordResetCompleteView.as_view(template_name='cuentas/password_reset_complete.html'), name='password_reset_complete'),
    path('', include('propiedadesApp.urls')),
    path('asesoria/', include('asesoriaApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
