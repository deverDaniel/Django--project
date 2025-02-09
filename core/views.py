from django.shortcuts import render,redirect
from .models import Pessoa,Veiculo, MovMensalista, Mensalista, MovRotativo
from .form import PessoaForm, VeiculoForm, MovRotativoForm, MensalistaForm, MovMensalistaForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from core.models import Veiculo
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.http import HttpResponse
import io
import csv


@login_required()
def home(request):
    context = {'mensagem': 'hello world'}
    return render(request, 'core/index.html', context)

@login_required()
def lista_pessoas(request):
    pessoas =  Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)

@login_required()
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoa')

@login_required()
def pessoa_update(request, id):
    data= {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form .is_valid():
            form.save()
            return redirect('core_lista_pessoa')
    else:
        return render(request, 'core/update_pessoa.html', data)

@login_required()
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        if request.method == "POST":
            pessoa.delete()
            return redirect('core_lista_pessoa')
    else:
        return render(request, 'core/delete_confirm.html', {"obj": pessoa})

@login_required()
def lista_veiculos(request):
    veiculos =  Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, "form": form}
    return render(request, 'core/lista_veiculos.html', data)

@login_required()
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculo')

@login_required()
def veiculo_update(request, id):
    data= {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form .is_valid():
            form.save()
            return redirect('core_lista_veiculo')
    else:
        return render(request, 'core/update_veiculo.html', data)

@login_required()
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        if request.method == "POST":
            veiculo.delete()
            return redirect('core_lista_veiculo')
    else:
        return render(request, 'core/delete_confirm.html', {"obj": veiculo})

@login_required()
def lista_movrotativos(request):
    movrotativos =  MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'movrotativos': movrotativos, "form":  form}
    return render(request, 'core/lista_movrotativo.html', data)

@login_required()
def movrotativo_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativo')

@login_required()
def movrotativo_update(request, id):
    data= {}
    movrotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=movrotativo)
    data['movrotativo'] = movrotativo
    data['form'] = form

    if request.method == 'POST':
        if form .is_valid():
            form.save()
            return redirect('core_lista_movrotativo')
    else:
        return render(request, 'core/update_movrotativo.html', data)

@login_required()
def movrotativo_delete(request, id):
    movrotativo = MovRotativo.objects.get(id=id)
    if request.method == 'POST':
        if request.method == "POST":
            movrotativo.delete()
            return redirect('core_lista_movrotativo')
    else:
        return render(request, 'core/delete_confirm.html', {"obj": movrotativo})

@login_required()
def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, "form":  form}
    return render(request, 'core/lista_mensalistas.html', data)

@login_required()
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')

@login_required()
def mensalista_update(request, id):
    data= {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == 'POST':
        if form .is_valid():
            form.save()
            return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/update_mensalista.html', data)

@login_required()
def mensalista_delete(request, id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalista')
    else:
        return render(request, 'core/delete_confirm.html', {"obj": mensalista})

@login_required()
def lista_movmensalista(request):
    movmensalistas =  MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'movmensalista': movmensalistas, "form":  form}
    return render(request, 'core/lista_movmensalista.html', data)

@login_required()
def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalista')

@login_required()
def movmensalista_update(request, id):
    data= {}
    movmensalista = MovMensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=  movmensalista)
    data['movmensalista'] = movmensalista
    data['form'] = form

    if request.method == 'POST':
        if form .is_valid():
            form.save()
            return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/update_movmensalista.html', data)

@login_required()
def movmensalista_delete(request, id):
    movmensalista = MovMensalista.objects.get(id=id)
    if request.method == 'POST':
        if request.method == "POST":
            movmensalista.delete()
            return redirect('core_lista_movmensalista')
    else:
        return render(request, 'core/delete_confirm.html', {"obj": movmensalista})


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):
    def get(self, request):
        veiculos = Veiculo.objects.all()
        params = {
            'veiculos': veiculos,
            'request': request,
        }
        return Render.render('core/relatorio.html', params, 'relatorio_veiculos')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        veiculos = Veiculo.objects.all()
        writer = csv.writer(response)
        writer.writerow(['Id', 'Marca', 'placa', 'Proprietario', 'Cor'])
        for veiculo in veiculos:
            writer.writerow(
                [veiculo.id, veiculo.marca, veiculo.placa, veiculo.proprietario,
                 veiculo.cor
                 ])
        return response
