from django.urls import path
from . import views
urlpatterns = [
	path('userlist/',views.userlist, name="userlist"),
	path('manage-user-account/', views.manageAccount, name="manageAccount"),
	path('change-user-password/', views.changeAccountPassword, name="changeAccountPassword"),
	# path('view-user-profile/', views.userProfile, name="userProfile"),
	

	path('reset-user-password/<str:id>', views.resetUserPassword, name="resetUserPassword"),
	path('delete-user/<str:id>', views.deleteUser, name="deleteUser"),
	path('ativu-user/<str:id>', views.ativuUser, name="ativuUser"),
	path('desativu-user/<str:id>', views.desativuUser, name="desativuUser"),

	path('Konfirma/Password/Utilizador/',views.KonfirmaPasswordProfile, name="KonfirmaPasswordProfile"),
	path('Update/Profile/Utilizador/',views.UpdateProfileUtilizador, name="UpdateProfileUtilizador"),
	path('Update/Photo/Profile/Utilizador/<str:hashid>',views.UpdateUserProfilePhoto, name="UpdateUserProfilePhoto"),

	path('register/admin/suku/', views.register_admin_suku, name='register_admin_suku'),

	
]