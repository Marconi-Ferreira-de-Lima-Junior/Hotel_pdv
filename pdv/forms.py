from django import forms
from .models import Cliente, Reserva, Quarto, Despesa, Receita

class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' #importa todos o campos do model
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder' : '000.000.000-00'}),
            'telefone' : forms.TextInput(attrs={'placeholder' : '(99)99999-9999'})
            }
        
class ReservaForm (forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

    def clean(self): #validação para que a data de entrada seja menor que a de saida e que o quarto esteja disponivel
        cleaned_data = super().clean()
        data_entrada = cleaned_data.get('data_entrada')
        data_saida = cleaned_data.get('data_saida')
        quarto = cleaned_data.get('quarto')

        if data_entrada and data_saida and data_saida <= data_entrada:
            raise forms.ValidationError("A data de saída deve ser maior que a de entrada.")

        if quarto and not quarto.esta_disponivel(data_entrada, data_saida):
            raise forms.ValidationError("Este quarto não está disponível no período selecionado.")

        return cleaned_data

class QuartoForm(forms.ModelForm):
    preco = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'R$ 0,00'}))

    class Meta:
        model = Quarto
        fields = '__all__'

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        try:
            preco = float(preco.replace('R$', '').replace(',', '.').strip())
        except ValueError:
            raise forms.ValidationError("Preço inválido.")
        return preco

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = '__all__'

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = '__all__'

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem.")

        return cleaned_data
        