from rest_framework import viewsets
from .models import Setor, Auditoria5S, ItemAuditoria, NaoConformidade, AcaoCorretiva
from .serializers import (
    SetorSerializer, Auditoria5SSerializer,
    ItemAuditoriaSerializer, NaoConformidadeSerializer,
    AcaoCorretivaSerializer
)

class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer


class Auditoria5SViewSet(viewsets.ModelViewSet):
    queryset = Auditoria5S.objects.all()
    serializer_class = Auditoria5SSerializer


class ItemAuditoriaViewSet(viewsets.ModelViewSet):
    queryset = ItemAuditoria.objects.all()
    serializer_class = ItemAuditoriaSerializer


class NaoConformidadeViewSet(viewsets.ModelViewSet):
    queryset = NaoConformidade.objects.all()
    serializer_class = NaoConformidadeSerializer


class AcaoCorretivaViewSet(viewsets.ModelViewSet):
    queryset = AcaoCorretiva.objects.all()
    serializer_class = AcaoCorretivaSerializer
