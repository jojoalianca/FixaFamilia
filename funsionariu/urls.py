from django.urls import path
from . import views


urlpatterns = [
	path('lista-Funsionariu/',views.ListaFunsionariu,name="ListaFunsionariu"),
	path('adisiona-Funsionariu/',views.AddFunsionariu,name="AddFunsionariu"),
	path('altera-dadus-Funsionariu/<str:hashid>',views.UpdateFunsionariu,name="UpdateFunsionariu"),

	path('lista-Detail-Funsionario/<str:id_fun>/', views.ViewFunsionario, name="ViewFunsionario"),
	path('Print-Detail-Funsionario/<str:id_fun>/', views.PrintDetalhoFun, name="PrintDetalhoFun"),

	# path('delete-fun/<str:id>', views.DeleteFun, name="DeleteFun"),


	
	path('ajax_load_work_area/',views.ajax_load_work_area,name="ajax_load_work_area"),

]