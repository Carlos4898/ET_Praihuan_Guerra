from django.contrib import admin
from .models import Categoria, Gato, Cliente

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Gato)
admin.site.register(Cliente)