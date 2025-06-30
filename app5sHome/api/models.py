from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class Auditoria5S(models.Model):
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    auditor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.setor.nome} - {self.data}"


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
