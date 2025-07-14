from django.db import models




class UserManager(models.Manager):
    def auditores(self):
        return self.filter(cargo='auditor')
    def leaders(self):
        return self.exclude(cargo='auditor')

class User(models.Model):
    USER_ROLES = [
        ('administrador', 'Administrador'),
        ('supervisor', 'Supervisor'),
        ('lider', 'Líder'),
        ('auditor', 'Auditor')
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    cargo = models.CharField(max_length=20, choices=USER_ROLES)
    is_active = models.BooleanField(default=True)
    objects = UserManager()
    def __str__(self):
        return f"{self.nome} ({self.cargo})"


class Setor(models.Model):
    SETORES = [
        ('adm', 'Administração'),
        ('producao', 'Produção'),
        ('manutencao', 'Manutenção'),
        ('ferramentaria', 'Ferramentaria'),
    ]
    nome = models.CharField(max_length=50, choices=SETORES)
    lider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='setores_liderados')
    def __str__(self):
        return self.nome


class Auditoria5S(models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.setor.nome} - {self.data.strftime('%d/%m/%Y')}"


class ItemAuditoria(models.Model):
    PILARES_5S = [
        ('seiri', 'Utilização'),
        ('seiton', 'Ordenação'),
        ('seiso', 'Limpeza'),
        ('seiketsu', 'Padronização'),
        ('shitsuke', 'Disciplina')
    ]
    notes = [
        (1, '1 - Muito Insatisfatório'),
        (2, '2 - Insatisfatório'),
        (3, '3 - Regular'),
        (4, '4 - Bom'),
        (5, '5 - Excelente')
    ]

    auditoria = models.ForeignKey(Auditoria5S, on_delete=models.CASCADE)
    senso = models.CharField(max_length=20, choices=PILARES_5S)
    nota = models.IntegerField(choices=notes, default=1)
    observacao = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.senso} - Nota: {self.nota}"


class NaoConformidade(models.Model):
    CRITICIDADES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta')
    ]
    item = models.ForeignKey(ItemAuditoria, on_delete=models.CASCADE, related_name='nao_conformidades')
    descricao = models.TextField()
    criticidade = models.CharField(max_length=20, choices=CRITICIDADES)
    data_detectada = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.criticidade} - {self.descricao[:30]}"


class AcaoCorretiva(models.Model):
    nao_conformidade = models.ForeignKey(NaoConformidade, on_delete=models.CASCADE, related_name='acoes_corretivas')
    descricao = models.TextField()
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    prazo = models.DateField()
    concluida = models.BooleanField(default=False)
    def __str__(self):
        status = 'Concluída' if self.concluida else 'Pendente'
        return f"{self.descricao[:30]} - {status}"
