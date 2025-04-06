from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from users.decorators import allowed_users
from django.contrib.auth.models import User,Group
from FixaApp.models import *
from django.db.models import Sum, Count
from custom.models import *
from django.db.models import Sum, F
from django.utils import timezone 
import datetime
 
@login_required()
def ReportTabular(request):  # Changed from 'filters' to 'request' for standard Django practice
    is_admin = request.user.is_superuser

    # Initialize base querysets
    if is_admin:
        # Admin sees all data
        total_seksu_Mane = DetCidadaun.objects.filter(seksu="Mane").count()
        total_seksu_Feto = DetCidadaun.objects.filter(seksu="Feto").count()
        data_suco = Village.objects.all()
        data_mun = ChefeFamilia.objects.all()
    else:
        try:
            # Non-admin users (Admin Suku) only see their village data
            admin_suku = request.user.adminsuku  # Access via OneToOne relation
            user_village = admin_suku.village
            
            total_seksu_Mane = DetCidadaun.objects.filter(
                seksu="Mane",
                village=user_village
            ).count()
            total_seksu_Feto = DetCidadaun.objects.filter(
                seksu="Feto",
                village=user_village
            ).count()
            data_suco = Village.objects.filter(id=user_village.id)
            data_mun = ChefeFamilia.objects.filter(village=user_village)
        except AdminSuku.DoesNotExist:
            # Handle case where user isn't an AdminSuku
            return render(request, 'error.html', {
                'message': 'You do not have permission to access this data'
            })

    # Prepare family data (same for both admin and non-admin)
    loopingCandidatoseksu = []
    for family in data_mun:
        total_Mane = DetCidadaun.objects.filter(
            chafeFAmila_id=family.id,
            seksu="Mane"
        ).count()
        total_Feto = DetCidadaun.objects.filter(
            chafeFAmila_id=family.id,
            seksu="Feto"
        ).count()
        total_estudante = DetCidadaun.objects.filter(
            chafeFAmila_id=family.id
        ).count()
        
        loopingCandidatoseksu.append({
            'id': family.id,
            'xefe_Familia': family.xefe_Familia,
            'total_seksu_Mane': total_Mane,
            'total_seksu_Feto': total_Feto,
            'total_estudante': total_estudante,
        })

    # Prepare village data (will only show the user's village for non-admins)
    loopingMembruFamiliaTuirSuco = []
    for village in data_suco:
        total_M = DetCidadaun.objects.filter(
            village_id=village.id,
            seksu="Mane"
        ).count()
        total_F = DetCidadaun.objects.filter(
            village_id=village.id,
            seksu="Feto"
        ).count()
        total = DetCidadaun.objects.filter(
            village_id=village.id
        ).count()
        
        loopingMembruFamiliaTuirSuco.append({
            'id': village.id,
            'name': village.name,
            'total_M': total_M,
            't_Feto': total_F,
            'total': total,
        })

    context = {
        "title": "REPORT TABULAR MEMBRU TUIR MONISIPIU",
        'konfigurasaunActive': "active",
        "data_mun": data_mun,
        'data_suco': data_suco,
        "loopingCandidatoseksu": loopingCandidatoseksu,
        "loopingMembruFamiliaTuirSuco": loopingMembruFamiliaTuirSuco,
        "total_seksu_Mane": total_seksu_Mane,
        "total_seksu_Feto": total_seksu_Feto,
        "is_admin": is_admin,
    }
    return render(request, 'tabular/ReportTabular.html', context)


#list combatente in Aldeia	
def public_membruFamilia_suku_aldeia(request,id):
	data_post=Village.objects.get(id=id)
	data_aldeia = Aldeia.objects.filter(village=data_post)
	totalFKAsukuM= DetCidadaun.objects.filter(village=data_post,seksu="Mane").count()
	totalFKAsukuF= DetCidadaun.objects.filter(village=data_post,seksu="Feto").count()
	totalFKAsuku= DetCidadaun.objects.filter(village=data_post).count()
	loopingFKAaldeia=[]
	for x in data_aldeia.iterator():
		total_sexo_Mane_mun = DetCidadaun.objects.filter(aldeia_id=x.id,seksu="Mane").count()
		total_sexo_Feto_mun= DetCidadaun.objects.filter(aldeia_id=x.id,seksu="Feto").count()
		totalFKA = DetCidadaun.objects.filter(aldeia_id=x.id).all().count()
		loopingFKAaldeia.append({'id':x.id,'name':x.name,
			'totalFKA':totalFKA,'total_sexo_Mane_mun':total_sexo_Mane_mun,'total_sexo_Feto_mun':total_sexo_Feto_mun,
			})
	context={
	"page":"list",'data_aldeia':data_aldeia,'data_post':data_post,'totalFKAsuku':totalFKAsuku,
	'totalFKAsukuM':totalFKAsukuM,'totalFKAsukuF':totalFKAsukuF,'loopingFKAaldeia':loopingFKAaldeia,
	}
	return render(request,'tabular/cidadaunaldeia.html',context) 



@login_required
def ReportgRAFIKO(request):
    # Data untuk village (Suku)
    village_data = Village.objects.all()
    village_stats = []

    for village in village_data:
        total_mane = DetCidadaun.objects.filter(village=village, seksu="Mane").count()
        total_feto = DetCidadaun.objects.filter(village=village, seksu="Feto").count()
        total_chefe = ChefeFamilia.objects.filter(village=village).count()

        # Jumlah total termasuk kepala keluarga
        total_warga = total_mane + total_feto + total_chefe

        village_stats.append({
            "id": village.id,
            "name": village.name,
            "total_mane": total_mane,
            "total_feto": total_feto,
            "total_warga": total_warga,  # Sudah termasuk kepala keluarga
        })

    # Data untuk aldeia
    aldeia_data = Aldeia.objects.all()
    aldeia_stats = []

    for aldeia in aldeia_data:
        total_mane = DetCidadaun.objects.filter(aldeia=aldeia, seksu="Mane").count()
        total_feto = DetCidadaun.objects.filter(aldeia=aldeia, seksu="Feto").count()
        total_chefe = ChefeFamilia.objects.filter(aldeia=aldeia).count()

        # Jumlah total termasuk kepala keluarga
        total_warga = total_mane + total_feto + total_chefe

        aldeia_stats.append({
            "id": aldeia.id,
            "name": aldeia.name,
            "total_mane": total_mane,
            "total_feto": total_feto,
            "total_warga": total_warga,  # Sudah termasuk kepala keluarga
        })

    context = {
        "title": "Relatoriu  Grafiku Total cidadaun (Inklui Chefe  Familia)",
        "village_stats": village_stats,
        "aldeia_stats": aldeia_stats,
    }

    return render(request, 'Grafiko/ReportGrafico.html', context)