from django.contrib import admin
from .models import Funsionariu,UserFunsionariu,Pozisaun
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.
class PozisaunResource(resources.ModelResource):
    class Meta:
        model = Pozisaun
class PozisaunAdmin(ImportExportModelAdmin):
    resource_class = PozisaunResource
admin.site.register(Pozisaun, PozisaunAdmin)

class FunsionariuResource(resources.ModelResource):
    class Meta:
        model = Funsionariu
class FunsionariuAdmin(ImportExportModelAdmin):
    resource_class = FunsionariuResource
admin.site.register(Funsionariu, FunsionariuAdmin)

class UserFunsionariuResource(resources.ModelResource):
    class Meta:
        model = UserFunsionariu
class UserFunsionariuAdmin(ImportExportModelAdmin):
    resource_class = UserFunsionariuResource
admin.site.register(UserFunsionariu, UserFunsionariuAdmin)