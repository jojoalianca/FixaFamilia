from django.shortcuts import render
from FixaApp.models import *
from django.db.models import Count, Q
from django.db.models import Sum, Count
from django.utils import timezone

def public_statistics(request):
    total_maneT = DetCidadaun.objects.filter(seksu="Mane").count()
    total_fetoT = DetCidadaun.objects.filter(seksu="Feto").count()
    total_populasaun = total_maneT + total_fetoT
    data_suco = Village.objects.all()
    data_mun = ChefeFamilia.objects.all()
    total_mane_percentage = (total_maneT / total_populasaun * 100) if total_populasaun > 0 else 0
    total_feto_percentage = (total_fetoT / total_populasaun * 100) if total_populasaun > 0 else 0
    suku_data = Village.objects.annotate(
        total_maneT=Count('detcidadaun', filter=Q(detcidadaun__seksu="Mane")),
        total_fetoT=Count('detcidadaun', filter=Q(detcidadaun__seksu="Feto"))
    ).values(
        'name', 'total_maneT', 'total_fetoT', 
    )
    suku_data = [
        {
            'name': suku['name'],
            'total_maneT': suku['total_maneT'],
            'total_fetoT': suku['total_fetoT'],
            'total': suku['total_maneT'] + suku['total_fetoT'],
            'percentage': ((suku['total_maneT'] + suku['total_fetoT']) / total_populasaun * 100) if total_populasaun > 0 else 0,

        }
        for suku in suku_data
    ]
    top_sukus = sorted(suku_data, key=lambda x: x['total'], reverse=True)[:10]
    gender_distribution = {
        'labels': ['Mane', 'Feto'],
        'data': [total_maneT, total_fetoT]
    }
    growth_rate = 2.5

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
            "total_maneT": total_maneT,
            "total_fetoT": total_fetoT,
            "total_warga": total_warga,  # Sudah termasuk kepala keluarga
        })

    context = {
        'total_maneT': total_maneT,
        'total_mane': total_mane,
        'total_feto': total_feto,
        'total_fetoT': total_fetoT,
        'total_populasaun': total_populasaun,
        'total_mane_percentage': total_mane_percentage,
        'total_feto_percentage': total_feto_percentage,
        'growth_rate': growth_rate,
        'suku_data': suku_data,
        'top_sukus': top_sukus,
        'gender_distribution': gender_distribution,
        'loopingMembruFamiliaTuirSuco': loopingMembruFamiliaTuirSuco,
        "village_stats": village_stats,
        "aldeia_stats": aldeia_stats,
        "data_suco": data_suco,
        "data_mun": data_mun,
        'current_time': timezone.now(),
    }
    
    return render(request, 'index_public.html', context)
