from django import forms
from .models import Cliente, Quarto, Reserva, Despesa, Receita

class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' #importa todos o campos do model
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder' : '000.000.000-00'}),
            'telefone' : forms.TextInput(attrs={'placeholder' : '(99)99999-9999'})
            }