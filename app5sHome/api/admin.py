from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Auditoria5S
from .forms import Auditoria5SForm

class Auditoria5SAdmin(admin.ModelAdmin):
    form = Auditoria5SForm

admin.site.register(Auditoria5S, Auditoria5SAdmin)
