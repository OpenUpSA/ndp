from django.contrib import admin
from ndp.models import Sector


class SectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Sector, SectorAdmin)
