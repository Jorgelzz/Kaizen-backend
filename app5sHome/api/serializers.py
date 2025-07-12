from rest_framework import serializers
from .models import Setor, Auditoria5S, ItemAuditoria, NaoConformidade, AcaoCorretiva, User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'


class Auditoria5SSerializer(serializers.ModelSerializer):

    qs = User.objects.filter(
        perfil_type='Auditor'
    )
    print(qs)

    class Meta:
        model = Auditoria5S
        fields = '__all__'


class ItemAuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAuditoria
        fields = '__all__'


class NaoConformidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaoConformidade
        fields = '__all__'


class AcaoCorretivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcaoCorretiva
        fields = '__all__'
