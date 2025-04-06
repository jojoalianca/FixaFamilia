from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from .utils import *
from users.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
# Create your views here.

@login_required()
@allowed_users(allowed_roles=['admin'])
def ListaSuku(request):
	group = request.user.groups.all()[0].name
	suku = Village.objects.all()
	context = {
		'group':group,
		'suku':suku,
		'sukuActive':"active",
		'title':"Lista Suku",
	}
	return render(request,'listasuku.html',context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def addSuku(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		form = SukuForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			username = instance.name
			instance.save()
			messages.info(request, f'Suku {username} is Added Successfully.')
			return redirect('listaSuku')
	else:
		form = SukuForm()
	context = {
		'sukuActive':"active",
		'page':"form",
		'group': group, 
		'form': form, 
	}
	return render(request, 'form_suku.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def updateSuku(request,hashid):
	group = request.user.groups.all()[0].name
	sukuData = get_object_or_404(Village,id=hashid)
	if request.method == 'POST':
		form = SukuForm(request.POST,instance=sukuData)
		if form.is_valid():
			instance = form.save()
			messages.info(request, f'Suku is updated Successfully.')
			return redirect('listaSuku')
	else:
		form = SukuForm(instance=sukuData)
	context = {
		'sukuActive':"active",
		'page':"form",
		'group': group, 
		'form': form, 
	}
	return render(request, 'form_suku.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def DeleteSuku(request, id_suku):
	suku = get_object_or_404(Village, id=id_suku)
	naran_suku = suku.name
	suku.delete()
	messages.warning(request, f'Suku {naran_suku} is Deleted Successfully.')
	return redirect('listaSuku')


@login_required()
@allowed_users(allowed_roles=['admin'])
def ListaAldeia(request):
	aldeia = Aldeia.objects.all()
	context = {
		'aldeiaActive':"active",
		'aldeia':aldeia,
		'title':"Lista Aldeia",
	}

	return render(request,'listaaldeia.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def AddAldeia(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		form = AldeiaForm1(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			username = instance.name
			instance.save()
			messages.success(request, f'Aldeia {username} is Added Successfully.')
			return redirect('listaAldeia')
	else:
		form = AldeiaForm1()
	context = {
		"group":group,
		'aldeiaActive':"active",
		'page':"form",
		'form': form, 
	}
	return render(request, 'form_aldeia.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def delete_aldeia(request, id_aldeia):
	data = Aldeia.objects.get(id=id_aldeia)
	name = data.name
	data.delete()
	messages.success(request, f'Aldeia {name} was deleted Successfully.')
	return redirect('listaAldeia')

@login_required
@allowed_users(allowed_roles=['admin'])
def Update_aldeia(request, hashid):
	group = request.user.groups.all()[0].name
	aldeia = get_object_or_404(Aldeia, id=hashid)
	name = aldeia.name
	if request.method == 'POST':
		form = AldeiaForm1(request.POST, instance=aldeia)
		if form.is_valid():
			form.save()
			messages.success(request, f'Aldeia {name} is updated Successfully.')
			return redirect('listaAldeia')
	else:
		form = AldeiaForm1(instance=aldeia)
	context = {
		"group":group,
		'aldeiaActive':"active",
		'page':"form",
		'form': form, 
	}
	return render(request, 'form_aldeia.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def listaMunisipiu(request):
	group = request.user.groups.all()[0].name
	munisipiu = Municipality.objects.all()
	context = {
		"group":group,
		'munisipiuActive':"active",
		'page':"list",
		'munisipiu':munisipiu,
		'title':"Lista Munisipiu",
	}

	return render(request,'munisipiu.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def addMunisipiu(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		form = MunisipiuForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			username = instance.name
			instance.save()
			messages.success(request, f'Munisipiu {username} is Added Successfully.')
			return redirect('listaMunisipiu')
	else:
		form = MunisipiuForm()
	context = {
		"group":group,
		'aldeiaActive':"active",
		'page':"form",
		'form': form, 
	}
	return render(request, 'munisipiu.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def deleteMunisipiu(request, id):
	data = Municipality.objects.get(id=id)
	name = data.name
	data.delete()
	messages.warning(request, f'Munisipiu {name} was deleted Successfully.')
	return redirect('listaMunisipiu')

@login_required
@allowed_users(allowed_roles=['admin'])
def updateMunisipiu(request, id):
	group = request.user.groups.all()[0].name
	munisipiu = get_object_or_404(Municipality, id=id)
	name = munisipiu.name
	if request.method == 'POST':
		form = MunisipiuForm(request.POST, instance=munisipiu)
		if form.is_valid():
			form.save()
			messages.success(request, f'Munisipiu {name} is updated Successfully.')
			return redirect('listaMunisipiu')
	else:
		form = MunisipiuForm(instance=munisipiu)
	context = {
		"group":group,
		'munisipiuActive':"active",
		'page':"form",
		'form': form, 
	}
	return render(request, 'munisipiu.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def listaPostu(request):
	group = request.user.groups.all()[0].name
	postu = AdministrativePost.objects.all()
	context = {
		"group":group,
		'postuActive':"active",
		'page':"list",
		'postu':postu,
		'title':"Lista Postu",
	}

	return render(request,'postu.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def addPostu(request):
	group = request.user.groups.all()[0].name
	if request.method == 'POST':
		form = PostuForm(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			username = instance.name
			instance.save()
			messages.success(request, f'Postu {username} is Added Successfully.')
			return redirect('listaPostu')
	else:
		form = PostuForm()
	context = {
		"group":group,
		'aldeiaActive':"active",
		'page':"form",
		'form': form, 
	}
	return render(request, 'postu.html', context)

@login_required
@allowed_users(allowed_roles=['admin'])
def deletePostu(request, id):
	data = AdministrativePost.objects.get(id=id)
	name = data.name
	data.delete()
	messages.warning(request, f'Postu {name} was deleted Successfully.')
	return redirect('listaPostu')

@login_required
@allowed_users(allowed_roles=['admin'])
def updatePostu(request, id):
	group = request.user.groups.all()[0].name
	postu = get_object_or_404(AdministrativePost, id=id)
	name = postu.name
	if request.method == 'POST':
		form = PostuForm(request.POST, instance=postu)
		if form.is_valid():
			form.save()
			messages.success(request, f'Postu {name} is updated Successfully.')
			return redirect('listaPostu')
	else:
		form = PostuForm(instance=postu)
	context = {
		"group":group,
		'postuActive':"active",
		'page':"form",
		'form': form, 
	}
	return render(request, 'postu.html', context)


@login_required
def load_posts(request):
	mun_id = request.GET.get('municipality')
	posts = AdministrativePost.objects.filter(municipality_id=mun_id).order_by('name')
	return render(request, 'posts_dropdown.html', {'posts': posts})

@login_required
def load_villages(request):
	post_id = request.GET.get('post')
	villages = Village.objects.filter(administrativepost_id=post_id).order_by('name')
	return render(request, 'villages_dropdown.html', {'villages': villages})

@login_required
def load_aldeias(request):
	village_id = request.GET.get('village')
	aldeias = Aldeia.objects.filter(village_id=village_id).order_by('name')
	return render(request, 'aldeias_dropdown.html', {'aldeias': aldeias})

@login_required
@allowed_users(allowed_roles=['admin'])
def konfigurasaun(request):
	totalMunisipiu = Municipality.objects.all().count()
	totalPostu = AdministrativePost.objects.all().count()
	totalSuku = Village.objects.all().count()
	totalAldeia = Aldeia.objects.all().count()
	context = {
		'konfigurasaunActive':"active",
		'totalMunisipiu': totalMunisipiu, 
		'totalPostu': totalPostu, 
		'totalSuku': totalSuku, 
		'totalAldeia': totalAldeia, 
	}
	return render(request, 'config.html', context)