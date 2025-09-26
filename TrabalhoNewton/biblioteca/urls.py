from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from livros.views import LivroViewSet, AutorViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'livros', LivroViewSet)
router.register(r'autores', AutorViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Biblioteca API",
        default_version='v1',
        description="API para CRUD de Livros e Autores",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]