from django.contrib import admin
from .models import *

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama', 'judul', 'body','kategory', 'date')
 
admin.site.register(Kategori)
admin.site.register(Artikel, ArtikelAdmin)
