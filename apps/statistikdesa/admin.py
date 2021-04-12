from django.contrib import admin

from .models import KartuKeluarga, Penduduk
# Register your models here.

class KkAdmin(admin.ModelAdmin):
    list_display = ['no_kk', 'nama_kk']

admin.site.register(KartuKeluarga, KkAdmin)
admin.site.register(Penduduk)

