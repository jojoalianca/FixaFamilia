from django.urls import path
from .views import *

urlpatterns = [
# suku
	path('konfigurasaun/', konfigurasaun, name="konfigurasaun"),
	path('lista-suku/', ListaSuku, name="listaSuku"),
	path('add-suku/', addSuku, name="addSuku"),
	path('update-suku/<str:hashid>', updateSuku, name="updateSuku"),
	path('delete-suku/<str:id_suku>', DeleteSuku, name="deleteSuku"),
	# aldeia
	path('lista-aldeia/', ListaAldeia, name="listaAldeia"),
    path('add_aldeia/', AddAldeia, name="AddAldeia"),
    path('delete_aldeia/<str:id_aldeia>/', delete_aldeia, name='deleteAldeia'),
    path('update-aldeia/<str:hashid>/', Update_aldeia, name='updateAldeia'),


	path('Lista-Munisipiu/', listaMunisipiu, name="listaMunisipiu"),
	path('Add-Munisipiu/', addMunisipiu, name="addMunisipiu"),
	path('Update-Munisipiu/<str:id>', updateMunisipiu, name="updateMunisipiu"),
	path('Delete-Munisipiu/<str:id>', deleteMunisipiu, name="deleteMunisipiu"),
	
	path('Lista-Postu/', listaPostu, name="listaPostu"),
	path('Add-Postu/', addPostu, name="addPostu"),
	path('Update-Postu/<str:id>', updatePostu, name="updatePostu"),
	path('Delete-Postu/S<str:id>', deletePostu, name="deletePostu"),

	path('ajax/load-posts/', load_posts, name='ajax_load_posts'),
	path('ajax/load-villages/', load_villages, name='ajax_load_villages'),
	path('ajax/load-aldeias/', load_aldeias, name='ajax_load_aldeias'),

]