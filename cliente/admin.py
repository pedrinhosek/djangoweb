# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from cliente.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    model = Cliente
    date_hierarchy = 'data_nascimento'

    # fields -> serve para informar quais campos deseja exibir no admin
    # fields = ('nome', 'data_nascimento', 'email')

    # exclude -> serve para informar quais campos deseja não exibir no admin
    # exclude = ('nome', 'data_nascimento')

    # list_display -> serve para informar quais campos deseja exibir na lista de apresentação
    list_display = ('id', 'nome', 'email', 'data_nascimento')

    # list_filter -> cria na lateral da pag um filtro com os campos informados
    list_filter = ('nome', 'email', 'data_nascimento')

    # readonly_fields -> serve para deixar os campos informados apenas como leitura
    # readonly_fields = ('nome',)

    # search_fields -> insere um campo de busca e permite a busca nos campos informados
    search_fields = ('nome', 'email')

admin.site.register(Cliente, ClienteAdmin)
