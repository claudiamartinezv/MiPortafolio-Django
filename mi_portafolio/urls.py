from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# importamos las vistas de la app portafolio
from portafolio import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
]

# servir archivos media y estáticos en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
