from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin_panel/', include('admin_panel.urls', namespace='admin_panel')),
    path('', TemplateView.as_view(template_name='core/landing.html'), name='landing')
]
