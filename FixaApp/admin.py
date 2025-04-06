from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

class CidadaunResource(resources.ModelResource):
    class Meta:
        model = DetCidadaun
class CidadaunAdmin(ImportExportModelAdmin):
    resource_class = CidadaunResource
admin.site.register(DetCidadaun, CidadaunAdmin)

admin.site.register(ChefeFamilia)
admin.site.register(Relegiao)
admin.site.register(HabilitasaunLiteraria)
admin.site.register(profissaun)
admin.site.register(Tinan)