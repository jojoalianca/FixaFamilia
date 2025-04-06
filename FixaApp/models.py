from django.db import models
from custom.models import *
from django.contrib.auth.models import User,AbstractUser


class Tinan(models.Model):
	name = models.CharField(max_length=100,null=True)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class profissaun(models.Model):
	name = models.CharField(max_length=100,null=True)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class Relegiao(models.Model):
	name = models.CharField(max_length=100,null=True)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class HabilitasaunLiteraria(models.Model):
	name = models.CharField(max_length=100,null=True)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)
 
class ChefeFamilia(models.Model):
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null=True,verbose_name="Munisipiu")
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null=True,verbose_name="Postu Administrativu")
	village = models.ForeignKey(Village, on_delete=models.CASCADE,null=True,verbose_name="Suku")
	tinan  = models.ForeignKey(Tinan, on_delete=models.CASCADE, null=True, blank=True)
	nu_Fixa = models.CharField(max_length=50, null=True, blank=True)
	xefe_Familia = models.CharField(max_length=100,null=True)
	aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE,null=True,blank=True)
	image = models.ImageField(upload_to='XefeFamilia/', null=True,blank=True)

	def __str__(self):
		template = '{0.xefe_Familia}'
		return template.format(self)
  
class DetCidadaun(models.Model):
	chafeFAmila= models.ForeignKey(ChefeFamilia, on_delete=models.CASCADE, null=True)
	naran = models.CharField(max_length=100,null=True)
	seksu = models.CharField(choices=[('Mane','Mane'),('Feto','Feto')],max_length=10,null=True,blank=True)
	relasaun = models.CharField(max_length=100, null=True , blank=True, verbose_name="Ralasaun Familia")
	Fatin_Moris = models.CharField(max_length=100, null=True , blank=True, verbose_name="Fatin Moris")
	Data_Moris = models.DateField(null=True , blank=True, verbose_name="Data , Fulan no Tinan Moris")
	EStadi_Civil = models.CharField(max_length=100, null=True , blank=True, verbose_name="Estadu Civil")
	Profisaun = models.ForeignKey(profissaun,on_delete=models.CASCADE, null=True , blank=True,)
	religiaun = models.ForeignKey(Relegiao, on_delete=models.CASCADE, null=True , blank=True, )
	habilitasaun = models.ForeignKey(HabilitasaunLiteraria, on_delete=models.CASCADE, null=True , blank=True, verbose_name="Habilitasaun Literaria")
	relasaun = models.CharField(max_length=100, null=True , blank=True, verbose_name="Ralasaun Familia")
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null=True,verbose_name="Munisipiu")
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null=True,verbose_name="Postu Administrativu")
	village = models.ForeignKey(Village, on_delete=models.CASCADE,null=True,verbose_name="Suku")
	aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE,null=True,blank=True)
	
	def __str__(self):
		template = '{0.naran}'
		return template.format(self)

