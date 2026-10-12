from django.shortcuts import render
import helloworld.models


def index(request):
    return lista_funcionarios(request)

def lista_funcionarios(request):
    # Primeiro, buscamos os funcionários
    funcionarios = helloworld.models.Funcionario.objects.all()

    # Incluímos os funcionários no contexto
    contexto = {'funcionarios': funcionarios}

    # Retornamos o template
    return render(request, "website/funcionarios.html", contexto)

from django.views.generic import ListView

class ListaFuncionarios(ListView):
    template_name = "website/funcionarios.html"
    model = helloworld.models.Funcionario
    context_object_name = "funcionarios"
    