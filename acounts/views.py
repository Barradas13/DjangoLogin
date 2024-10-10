from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .models import Pessoa
from django.http import  HttpRequest

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'htmls/cadastro.html')
    
    username= request.POST.get('nome')
    nomesobrenome= request.POST.get('sobrenome')
    data= request.POST.get('data')
    texto= request.POST.get('texto')
    email= request.POST.get('email')
    imagem = request.FILES.get('imagem')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if senha != senha2:
        messages.add_message(request, constants.ERROR,'Verifique sua senha!')
        return render(request, 'htmls/cadastro.html')

    if len(senha) < 6:
        messages.add_message(request, constants.ERROR,'Sua senha esta muito fraca!')
        return render(request, 'htmls/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.add_message(request, constants.ERROR,'ja temos um usuario cadastrado nesse email')
        return render(request, 'htmls/cadastro.html')

    if User.objects.filter(username=username).exists():
        messages.add_message(request, constants.ERROR,'ja temos um usuario cadastrado nesse username')
        return render(request, 'htmls/cadastro.html')
    data_ano = data.split('-')
    if len(data_ano[0]) != 4:
        messages.add_message(request, constants.ERROR,'O ano da sua data deve conter 4 numeros')
        return render(request, 'htmls/cadastro.html')
    try:
        validate_email(email)
    except:
        messages.add_message(request, constants.ERROR,'por favor digite um email valido')
        return render(request, 'htmls/cadastro.html')

    user= User.objects.create_user(username=username, email=email, password=senha, last_name=nomesobrenome)
    user.save()
    messages.add_message(request, constants.SUCCESS,'SUCESSO')
    print(imagem, data)
    Pessoa.objects.create(usuario=user, texto=texto, DataNasci=data, imagem = imagem)

    return redirect('login')

def login(request):
    if request.method != 'POST':
        return render(request, 'htmls/login.html')
    
    username = request.POST.get('nome')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    user = auth.authenticate(request, username=username, password = senha)
    
    if senha != senha2:
        messages.add_message(request, constants.ERROR,'Suas senhas estão erradas!')
        return render(request, 'htmls/login.html')

    
    if user:
        auth.login(request, user)
        return redirect('dashboard')
    else:
        messages.add_message(request, constants.ERROR,'Seus dados estão errados!')
        return render(request, 'htmls/login.html')

@login_required(redirect_field_name='login')
def dashboard(request):
    
    id  =request.user.id
    pessoa = get_object_or_404(Pessoa, usuario_id = id)
    if request.method != 'POST':
        pessoa = get_object_or_404(Pessoa, usuario_id = id)
        return render(request, 'htmls/dashboard.html', {'Pessoa':pessoa})
        
    data= request.POST.get('data')
    texto= request.POST.get('text')

    try:
        imagem = request.FILES.get('imagem')
    except:
        pass

    if data:
        data_ano = data.split('-')
        if len(data_ano[0]) != 4:
            messages.add_message(request, constants.ERROR,'O ano da sua data deve conter 4 numeros')
            return render(request, 'htmls/dashboard.html', {'Pessoa':pessoa})

    if data and texto and imagem:
        pessoa = get_object_or_404(Pessoa, usuario_id = id)
        pessoa.texto =texto
        pessoa.imagem =imagem
        pessoa.DataNasci= data
        pessoa.save()
        messages.add_message(request, constants.SUCCESS,'Seus dados foram alterados com sucesso!')
        return render(request, 'htmls/dashboard.html', {'Pessoa':pessoa})

    if not imagem and data and texto:
        pessoa = get_object_or_404(Pessoa, usuario_id = id)
        pessoa.texto =texto
        pessoa.DataNasci =data
        pessoa.save()
        messages.add_message(request, constants.SUCCESS,'Seus dados foram alterados com sucesso!')
        return render(request, 'htmls/dashboard.html', {'Pessoa':pessoa})

    if not data and imagem and texto:
        pessoa = get_object_or_404(Pessoa, usuario_id = id)
        pessoa.texto =texto
        pessoa.imagem =imagem
        pessoa.save()
        messages.add_message(request, constants.SUCCESS,'Seus dados foram alterados com sucesso!')
        return render(request, 'htmls/dashboard.html', {'Pessoa':pessoa})

    if not data and not imagem:
        pessoa = get_object_or_404(Pessoa, usuario_id = id)
        pessoa.texto =texto
        pessoa.save()
        messages.add_message(request, constants.SUCCESS,'Seus dados foram alterados com sucesso!')
        return render(request, 'htmls/dashboard.html', {'Pessoa':pessoa})

    messages.add_message(request, constants.ERROR,'Ocorreu um erro ao tentar mudar alguns dados')
    return render(request, 'htmls/dashboard.html', {'Pessoa':pessoa})