from django.db import models


class User(models.Model):

    type_user = [
        ('Administrador', 'Administrador'),
        ('Supervisor', 'Supervisor'),
        ('Líder', 'Líder'),
        ('Auditor','Auditor')
    ]

    responsavel = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    perfil_type = models.CharField(max_length=20, choices=type_user)
    status = models.BooleanField() # Descreve se o login atual é ativo ou não

    def __str__(self):
        return f"{self.responsavel} - {self.perfil_type}"

class Setor(models.Model):
    setores = [
        ('Adm','Administração'),
        ('Produção', 'Produção'),
        ('Manutenção', 'Manutenção'),
        ('Ferramentaria', 'Ferramentaria'),
    ]

    setor_name = models.CharField(max_length=100, choices=setores)
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.setor_name


class Auditoria5S(models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    responsavel = User.responsavel
    data = models.DateField(auto_now_add=True)
    perfil_type = models.ForeignKey(User, on_delete=models.CASCADE, related_name='type_user')

    def __str__(self):
        return f"{self.setor.setor_name} - {self.data}"


class ItemAuditoria(models.Model):
    PILARES = [
        ('Seiri', 'Utilização'),
        ('Seiton', 'Ordenação'),
        ('Seiso', 'Limpeza'),
        ('Seiketsu', 'Padronização'),
        ('Shitsuke', 'Disciplina')
    ]

    auditoria = models.ForeignKey(Auditoria5S, on_delete=models.CASCADE, related_name="itens")
    pilar = models.CharField(max_length=20, choices=PILARES)
    nota = models.IntegerField()  # Escala de 0 a 5, por exemplo
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pilar} - Nota: {self.nota}"


class NaoConformidade(models.Model):
    CRITICIDADES = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta')
    ]

    item = models.ForeignKey(ItemAuditoria, on_delete=models.CASCADE)
    descricao = models.TextField()
    criticidade = models.CharField(max_length=20, choices=CRITICIDADES)
    data_detectada = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.criticidade} - {self.descricao[:30]}"


class AcaoCorretiva(models.Model):
    nao_conformidade = models.ForeignKey(NaoConformidade, on_delete=models.CASCADE)
    descricao = models.TextField()
    responsavel = models.CharField(max_length=100)
    prazo = models.DateField()
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.descricao[:30]} - {'Concluída' if self.concluida else 'Pendente'}"
