from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Setor, Auditoria5S, ItemAuditoria, NaoConformidade, AcaoCorretiva, User
from .serializers import (
    SetorSerializer, Auditoria5SSerializer,
    ItemAuditoriaSerializer, NaoConformidadeSerializer,
    AcaoCorretivaSerializer, UserSerializer

)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def auditores(self, request):
        auditores = self.get_queryset().filter(cargo='auditor')
        serializer = self.get_serializer(auditores, many=True)
        return Response(serializer.data)
    @action(detail=False)
    def leaders(self, request):
        leaders = self.get_queryset().exclude(cargo='auditor')
        serializer = self.get_serializer(leaders, many=True)
        return Response(serializer.data)

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
