from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from FixaApp.models import *
from .forms import *
from django.contrib.auth.models import User,Group
from custom.utils import *
from custom.models import *
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users

# Create your views here.
@login_required
@allowed_users(allowed_roles=['admin', 'Admin Suku'])
def ListaXefeFamilia(request):
    listaXF = ChefeFamilia.objects.all()

    # Define is_admin (for example, checking if the user is an admin)
    is_admin = request.user.is_superuser  # Assuming you're checking if the user is a superuser/admin

    context = {
        "title": "Lista Xefe Familia",
        "active_funsionariu": "active",
        "page": "list",
        "listaXF": listaXF,
        "is_admin": is_admin,
    }

    return render(request, "lista_xefeFamilia.html", context)
@login_required
def addxefeFamilia(request):
    user_groups = request.user.groups.values_list('name', flat=True)  # Ambil semua grup user
    
    if request.method == 'POST':
        _, newid = getlastid(ChefeFamilia)
        hashid = hash_md5(str(newid))
        
        if "admin" in user_groups:
            form = XefeFamilia_Form(request.POST, request.FILES)
        elif "Admin Suku" in user_groups:
            form = ChefeFamiliaForm1(request.POST, request.FILES, user=request.user)
        else:
            messages.error(request, "Akses tidak diizinkan.")
            return redirect('ListaXefeFamilia')
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.hashed = hashid
            instance.user_created = request.user
            instance.save()
            messages.success(request, f'Dadus Xefe Familia {instance.xefe_Familia} Rejistu ho Susesu.')
            return redirect('ListaXefeFamilia')
    else:
        if "admin" in user_groups:
            form = XefeFamilia_Form()
        elif "Admin Suku" in user_groups:
            form = ChefeFamiliaForm1(user=request.user)
        else:
            messages.error(request, "Akses tidak diizinkan.")
            return redirect('ListaXefeFamilia')
    
    context = {
        "group": user_groups,
        'aldeiaActive': "active",
        'page': "form",
        'form': form, 
    }
    return render(request, 'lista_xefeFamilia.html', context)

@login_required
def add_Membro_familia(request, id1):
	if request.method == 'POST':
		get_student = ChefeFamilia.objects.get(id=id1)
		form = membroFamiliaForm(request.POST, request.FILES) 
		if form.is_valid():
			instance = form.save(commit=False)
			instance.chafeFAmila = get_student
			instance.save()
			id1 = instance.chafeFAmila.id
			messages.success(request, f'Dokumet Filiasaun Mae is Added Successfully.')
			return redirect('detailViewsFixa',id1 )
	else:
		form = membroFamiliaForm() 
	context = {
		'aldeiaActive':"active",
		'page':"form",
		'form': form, 
	}
	return render(request, 'XefeFamilia/formMebroFamilia.html', context)



@login_required
def detailViewsFixa(request, id_est):
    is_admin = request.user.is_superuser
    est = get_object_or_404(ChefeFamilia, id=id_est)
    detailest = DetCidadaun.objects.filter(chafeFAmila=est).all()
    context = {
        'est': est,
        'detailest': detailest,
        'is_admin': is_admin,
    }
    return render(request, 'XefeFamilia/detail_Fixa.html', context)
# views.py
@login_required
def update_MembroFamilia(request, pk):
    detcidadaun = get_object_or_404(DetCidadaun, pk=pk)
    if request.method == 'POST':
        form = membroFamiliaForm(request.POST, instance=detcidadaun)
        if form.is_valid():
            form.save()
            messages.success(request, 'membro Familia Is Update Successfully.')
            return redirect('ListaXefeFamilia',)  # Adjust the redirect target as needed
    else:
        form = membroFamiliaForm(instance=detcidadaun)
    
    return render(request, 'XefeFamilia/formMebroFamilia.html', {'form': form,'detcidadaun':detcidadaun,})

@login_required()
def deleteMembroFamilia(request, pk):
	est = get_object_or_404(DetCidadaun, id=pk)
	naran = est.naran
	est.delete()
	messages.warning(request, f'Membru Familia {naran} is Deleted Successfully.')
	return redirect('ListaXefeFamilia')

@login_required
def PrintFixa(request, id_est):
    est = get_object_or_404(ChefeFamilia, id=id_est)
    detailest = DetCidadaun.objects.filter(chafeFAmila=est).all()
    context = {
        'est': est,
        'detailest': detailest,
    }
    return render(request, 'XefeFamilia/Print_Fixa.html', context)
