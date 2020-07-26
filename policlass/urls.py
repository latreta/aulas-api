"""policlass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from aulas.api.viewsets import AulasViewSet
from blocos.api.viewsets import BlocosViewSet
from cadeiras.api.viewsets import CadeirasViewSet
from discentes.api.viewsets import DiscentesViewSet
from salas.api.viewsets import SalasViewSet

router = routers.DefaultRouter()
router.register(r'blocos', BlocosViewSet)
router.register(r'salas', SalasViewSet)
router.register(r'discentes', DiscentesViewSet)
router.register(r'cadeiras', CadeirasViewSet)
router.register(r'aulas', AulasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
