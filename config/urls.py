
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from apps.projects.views import ProjectViewSet
from apps.materials.views import MaterialViewSet


router = DefaultRouter()

router.register(r'projects', ProjectViewSet)
router.register(r'materials', MaterialViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/v1/auth/', include('apps.accounts.urls')),

    path('api/v1/', include(router.urls)),
]

urlpatterns += [

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
]