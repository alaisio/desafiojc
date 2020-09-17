import json, requests, time
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserPasswordChangeForm
from users.models import CustomUser
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.

def importar(request):

    listusers = CustomUser.objects.filter().order_by('-id')[:10]

    if not request.user.is_superuser:
        messages.error(request, ('Desculpe, você não tem permissão para importar clientes')) 
        return redirect('index')
        
    else:
        url = requests.get('https://jsonplaceholder.typicode.com/users')
        lista = url.json()
        with open('users/bd_clientes.json', 'w') as json_file:
            json.dump(lista, json_file, indent=4)
        
        print('Criando arquivo a ser importado...')
        time.sleep(2)
        
        with open('users/bd_clientes.json') as json_file:
            clientes = json.load(json_file)
            for item in clientes:
                #print(item['username'])
                newusers = {'username': item['username'],
                        'email': item['email'],
                        'name': item['name'],
                        'password1': 'senhapadrao!',
                        'password2': 'senhapadrao!',
                }
                uform = CustomUserCreationForm(newusers)
                if uform.is_valid():
                    uform.save()
        messages.success(request, ('Importação concluída com sucesso!'))

    return render(request, 'importar.html', {
        'listusers': listusers,
    })


def minhaconta(request):
    if not request.user.is_authenticated:     
        return redirect('index')
    else:
        if request.method == 'POST':
            form_profile = CustomUserChangeForm(request.POST, instance=request.user)
            if form_profile.is_valid():
                form_profile.save()
                messages.success(request, ('Seu perfil foi atualizado com sucesso!'))
                return redirect('minhaconta')
            else:
                messages.error(request, ('Por favor, corrija os erros abaixo.'))
        else:
            form_profile = CustomUserChangeForm(instance=request.user)
        return render(request, 'minhaconta.html', {
            'form_profile': form_profile
             })


def alterarsenha(request):
    if not request.user.is_authenticated:     
        return redirect('index')
    else:
        if request.method == 'POST':
            form_asenha = CustomUserPasswordChangeForm(user=request.user, data=request.POST)
            if form_asenha.is_valid():
                form_asenha.save()
                messages.success(request, ('Sua senha foi alterada com sucesso! '))
                messages.success(request, ('Identifique-se com a nova senha'))
                return redirect('index')
                
            else:
                messages.error(request, ('Por favor, corrija os erros abaixo.'))
                
        else:
            form_asenha = CustomUserPasswordChangeForm(user=request.user)

        return render(request, 'alterarsenha.html', {
            'form_asenha': form_asenha      
            })


def index(request):
    if request.user.is_authenticated:
        return redirect('minhaconta')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.error(request, ('Sua conta está inativa'))
                    return render(request, 'index.html')
            else:
                messages.error(request, ('Login Inválido'))
                return render(request, 'index.html')
        return render(request, 'index.html')

    return render(request, 'index.html')


def logout_user(request):
    logout(request)
    form = CustomUser(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('index')
