from django.urls import path
from . import views

urlpatterns = [
	path ('Lista/Xefe/Familia',views.ListaXefeFamilia, name='ListaXefeFamilia'),
	path('Adisiona-xefe-Familia/', views.addxefeFamilia, name="addxefeFamilia"),
	path('Adisiona-Membro-Familia/<str:id1>', views.add_Membro_familia, name="add_Membro_familia"),
	path('Detail-View-Fixa-Familia/<str:id_est>/', views.detailViewsFixa, name='detailViewsFixa'),
	path('update_membru-Familia/<int:pk>/', views.update_MembroFamilia, name='update_MembroFamilia'),
	path('delete_membru-Familia/<int:pk>/', views.deleteMembroFamilia, name='deleteMembroFamilia'),
	path('print-Familia/<int:id_est>/', views.PrintFixa, name='PrintFixa'),

]