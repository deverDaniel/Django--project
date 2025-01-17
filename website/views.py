from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def contato(request):
    return render(request, 'website/contato.html')
def servico(request):
    return render(request, 'website/servico.html')
def sobre(request):
    return render(request, 'website/sobre.html')
def plano(request):
    return render(request, 'website/plano.html')
