from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from combatente.models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from django.db.models import Sum, Count

# Create your views here.
@login_required(login_url='login') 
def index(request):
	is_admin = request.user.is_superuser
	context = {

		"title":"SR-FIXA FAMILIA  ",
		'konfigurasaunActive':"active",  
		'is_admin':is_admin,  
	}
	return render(request, 'home/index.html',context)

#repot list estudnte print tinan
