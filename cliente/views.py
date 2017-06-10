# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from cliente.models import Cliente
from cliente.forms import ClienteForm


def home(request):
    return HttpResponse('SISTEMA DE CLIENTES')


def cliente_lista(request):
    data = {}
    data['lista_clientes'] = Cliente.objects.all()
    return render(request, 'cliente.html', data)


def cliente_update(request, pk):
    cliente = Cliente.objects.get(id=pk)

    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('cliente_lista')
    return render(request, 'cliente_detalhe.html', {'object':cliente, 'form': form})
    # return render(request, 'cliente_detalhe.html', {'object': cliente})


def cliente_create(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('cliente_lista')
    return render(request, 'cliente_novo.html', {'form':form})


def cliente_delete(request, pk):
    cliente = Cliente.objects.get(id=pk)

    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_lista')
    return render(request, 'cliente_delete_confirm.html', {'object': cliente})