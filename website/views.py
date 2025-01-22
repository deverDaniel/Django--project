from django.shortcuts import render
from .models import Contato


def home(request):
    return render(request, 'website/index.html')

def contato(request):
    mensagem = ''
    if request.method == 'POST':
        try:
            contato = {}
            contato['nome'] = request.POST.get('nome')
            contato['email'] = request.POST.get('email')
            contato['telefone'] = request.POST.get('telefone')
            contato['mensagem'] = request.POST.get('mensagem')
            Contato.objects.create(**contato)
            mensagem = 'contato realizado com sucesso'
        except Exception as e:
            mensagem = str(e)
        print(f"Mensagem enviada ao template: {mensagem}")
    return render(request, 'website/contato.html', {'mensagem': mensagem})
def servico(request):
    return render(request, 'website/servico.html')
def sobre(request):
    return render(request, 'website/sobre.html')
def plano(request):
    return render(request, 'website/plano.html')

