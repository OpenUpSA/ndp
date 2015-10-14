from django.contrib import admin
from ndp.models import Sector, Project, Organisation


class SectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Sector, SectorAdmin)
admin.site.register(Organisation, admin.ModelAdmin)
admin.site.register(Project, admin.ModelAdmin)
