from django.shortcuts import render, redirect
from .models import Pessoa, Veiculo, MovRotativo, Mensalista, MovMensalista
from .forms import PessoaForm, VeiculoForm, MovRotativoForm, MensalistaForm, MovMensalistaForm

def index(request):
    return render(request, 'index.html')


def pessoa(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    return render(request, 'pessoa.html', context={
        'pessoas': pessoas,
        'form': form
    })


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('pessoa')  

 
def pessoa_update(request, id):
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pessoa')   
    else:
        return render(request, 'update_pessoa.html', context={
            'pessoa': pessoa,
            'form': form
        })
    

def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('pessoa')   
    else:
        return render(request, 'delete_confirm.html', context={
            'obj': pessoa
        })
 

def veiculo(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    return render(request, 'veiculo.html', context={
        'veiculos': veiculos,
        'form': form
    })


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('veiculo') 


def veiculo_update(request, id):
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('veiculo')   
    else:
        return render(request, 'update_veiculo.html', context={
            'veiculo': veiculo,
            'form': form
        })
    

def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)

    if request.method == 'POST':
        veiculo.delete()
        return redirect('veiculo')   
    else:
        return render(request, 'delete_confirm.html', context={
            'obj': veiculo
        })


def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    return render(request, 'movrotativos.html', context={
        'mov_rot': mov_rot,
        'form': form
    })


def movrotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('mov_rot') 


def movrotativo_update(request, id):
    mov_rotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov_rotativo)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('mov_rot')   
    else:
        return render(request, 'update_movrotativo.html', context={
            'mov_rotativo': mov_rotativo,
            'form': form
        })
    

def movrotativo_delete(request, id):
    mov_rot = MovRotativo.objects.get(id=id)

    if request.method == 'POST':
        mov_rot.delete()
        return redirect('mov_rot')   
    else:
        return render(request, 'delete_confirm.html', context={
            'obj': mov_rot
        })    


def mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    return render(request, 'mensalista.html', context={
        'mensalistas': mensalistas,
        'form': form
    })


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('mensalista') 


def mensalista_update(request, id):
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('mensalista')   
    else:
        return render(request, 'update_mensalista.html', context={
            'mensalista': mensalista,
            'form': form
        })
    

def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)

    if request.method == 'POST':
        mensalista.delete()
        return redirect('mensalista')   
    else:
        return render(request, 'delete_confirm.html', context={
            'obj': mensalista
        })      


def mov_mensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    return render(request, 'mov_mensalista.html', context={
        'mov_mensalistas': mov_mensalistas,
        'form': form
    })


def mov_mensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('mov_mensalista') 


def movmensalista_update(request, id):
    mov_mensal = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensal)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('mov_mensalista')   
    else:
        return render(request, 'update_movmensalista.html', context={
            'mov_mensal': mov_mensal,
            'form': form
        })
    

def movmensalista_delete(request, id):
    mov_mensal = MovMensalista.objects.get(id=id)

    if request.method == 'POST':
        mov_mensal.delete()
        return redirect('mov_mensalista')   
    else:
        return render(request, 'delete_confirm.html', context={
            'obj': mov_mensal
        })   
