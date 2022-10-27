from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Register your models here.
from .models import (
    Filme,
    Locacao,
    LocacaoFilme,
    Categoria,
    Cliente,
)
# Register your models here.
 
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Filme)
admin.site.register(LocacaoFilme)
admin.site.register(Locacao)