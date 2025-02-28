from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth import User 
from .models import Cliente, Reserva, Quarto, Despesa, Receita
from .forms import ClienteForm, ReservaForm, UserRegistrationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard') #direciona para o painel principal caso não haja usuario cadastrado
        return render(request, 'hotel_transilvania_pdv/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login') #redireciona para pagina de login apos fazer o logout

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_passwordd(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'hotel_transilvania_pdv/register.html', {'form':form}) 

#dashboard - reservas e ocupação
@login_required
def dashboard(request):
    total_clientes = Cliente.objects.count()
    total_reserva = Reserva.objects.count()
    quartos_disponiveis = Quarto.objects.filter(disponivel=True).count()#filtra os quartos disponiveis

    return render(request,'hotel_transilvania_pdv/dashboard.html', {
        'total_clientes':total_clientes,
        'total_reserva':total_reserva,
        'quartos_disponiveis':quartos_disponiveis   
    })

#listando os clientes
@login_required
def clientes_view(request):
    clientes = clientes.objects.all()
    return render(request, 'hotel_transilvania_pdv/clientes.html', {'clientes':clientes})

#cadastro de clientes
@login_required
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'hotel_transilvania_pdv/cadastrar_cliente.html', {'form':form})

@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id = id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente) #cria um formulario preenchido com os dados novos dos clientes que foram enviados pelo usuario, referenciando ao cliente que ja existe  instance = cliente
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render (request, 'hotel_transilvania_pdv/editar_cliente.html', {'form': form})

@login_required
def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method =='POST':
        Cliente.delete()
        return redirect('clientes')
    return render (request, 'hotel_transilvania_pdv/confirmar_exclusao.html', {'cliente':cliente})

#reservas - listar as reservas existentes
@login_required
def reservas_view(request):
    reservas = Reserva.objects.all()
    return render (request, 'hotel_transilvania_pdv/reservas.html',{'reservas':reservas})

#criar as reservas
@login_required
def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm()

    return render (request, 'hotel_transilvania_pdv/criar_reserva.html', {'form':form})

@login_required
def editar_reserva(request,id):
    reserva = get_objects_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance = reserva)
        if form.is_valid():
            form.save()
            return redirect ('reservas')
    else:
        form = ReservaForm(instance = reserva)
    return render (request, 'hotel_transilvania_pdv/editar_reserva.html', {'form':form})

@login_required
def excluir_reserva(request,id):
    reserva = get_objects_or_404(Reserva, id = id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reservas')
    return render (request, 'hotel_transilvania_pdv/confirmar_exclusao.html', {'reserva': reserva})

#faturamento total do hotel
@login_required
def relatorios_view(request):
    total_receitas = sum(receita.valor for receita in Receita.objects.all())
    total_despesas = sum(despesa.valor for despesa in Despesa.objects.all())
    saldo_total = total_receitas - total_despesas

    return render (request, 'hotel_transilvania_pdv/relatorios.html', {
        'total_receitas':total_receitas,
        'toal_despesas':total_despesas,
        'saldo_total':saldo_total
    })



