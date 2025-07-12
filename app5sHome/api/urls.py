from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SetorViewSet, Auditoria5SViewSet, ItemAuditoriaViewSet,
    NaoConformidadeViewSet, AcaoCorretivaViewSet, UserViewSet
)

router = DefaultRouter()
router.register(r'setores', SetorViewSet)
router.register(r'auditorias', Auditoria5SViewSet)
router.register(r'itens', ItemAuditoriaViewSet)
router.register(r'nao-conformidades', NaoConformidadeViewSet)
router.register(r'acoes-corretivas', AcaoCorretivaViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
