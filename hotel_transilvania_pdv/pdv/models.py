from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Quarto(models.Model):
    numero = models.CharField(max_length=5)
    tipo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.numero
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField()

    def __str__(self):
        return f"Reserva de {self.cliente.nome} no quarto {self.quarto.numero}"
    
    def clean(self):
        if self.data_saida <= self.data_entrada:
            raise ValidationError ("A data de saída deve ser maior que a de entrada.")

class Despesa(models.Model):
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.descricao

class Receita(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, null=True, blank=True)
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return self.descricao
