from django.contrib import admin
from .models import Celular
from .models import Marca

# Register your models here.
admin.site.register(Celular)
admin.site.register(Marca)