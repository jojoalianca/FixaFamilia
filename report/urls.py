from django.urls import path
from .views import *

urlpatterns = [
	path('Report-Tabular-Candidatos-munisipiu/', ReportTabular, name="ReportTabular"),	
	path('Report-Grafiko-Candidatos-munisipiu/', ReportgRAFIKO, name="ReportgRAFIKO"), 	
	path('Report-tabular-cidadaun-Aldeia/<str:id>', public_membruFamilia_suku_aldeia, name="public_membruFamilia_suku_aldeia"), 	
]
