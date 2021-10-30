from django.contrib import admin
from cadastro_frete.models import CadastroEmpresa,CadastroCliente,CadastroOferta,Lance

# Register your models here.
class Empresas(admin.ModelAdmin):
    list_display = ('id', 'name', 'doc', 'about', 'site', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('name','doc',)
    list_filter = ('active',)
    list_editable = ('active',)
    list_per_page = 10
    ordering = ('name',)

admin.site.register(CadastroEmpresa, Empresas)

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'name', 'doc', 'about', 'site', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('name','doc',)
    list_filter = ('active',)
    list_editable = ('active',)
    list_per_page = 10
    ordering = ('name',)

admin.site.register(CadastroCliente, Clientes)

class Ofertas(admin.ModelAdmin):
    list_display = ('id_customer', 'from_de', 'to_para', 'initial_value', 'amount', 'amount_type')
    list_display_links = ('id_customer',)
    search_fields = ('id_customer',)
    list_filter = ()
    list_editable = ()
    list_per_page = 10
    ordering = ()

admin.site.register(CadastroOferta, Ofertas)

class Lances(admin.ModelAdmin):
    list_display = ('id_provider', 'id_offer', 'value', 'amount')
    list_display_links = ('id_provider','id_offer')
    search_fields = ('id_provider','id_offer',)
    list_filter = ()
    list_editable = ()
    list_per_page = 10
    ordering = ()

admin.site.register(Lance, Lances)