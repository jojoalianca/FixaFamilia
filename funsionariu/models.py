from django.db import models
from custom.models import *
from django.contrib.auth.models import User 


# Create your models here.
class Pozisaun(models.Model):
	naran = models.CharField(max_length=100,null=True)
	def __str__(self):
		template = '{0.naran}'
		return template.format(self) 

class Funsionariu(models.Model):
	naran = models.CharField(max_length=200, null=True)
	seksu = models.CharField(choices=[('Mane','Mane'),('Feto','Feto')],max_length=10,null=True,blank=True)
	pozisaun = models.ForeignKey(Pozisaun, null=True,on_delete=models.CASCADE)
	aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE,null=True,blank=True)
	village = models.ForeignKey(Village, on_delete=models.CASCADE,null=True,related_name="Village",verbose_name="Suku")
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null=True,related_name="AdministrativePost",verbose_name="Postu Administrativu")
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null=True,related_name="Municipality",verbose_name="Munisipiu")
	areamunicipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null=True,related_name="AreaMunicipality",blank=True,verbose_name="Area Servisu (Munisipiu)")
	areaadministrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null=True,related_name="AreaAdministrativePost",blank=True,verbose_name="Area Servisu (Postu)")
	areavillage = models.ForeignKey(Village, on_delete=models.CASCADE,null=True,related_name="AreaVillage",blank=True,verbose_name="Area Servisu (Suku)")
	email = models.CharField(max_length=200, null=True)
	nu_telefone = models.CharField(max_length=200, null=True)
	is_active = models.BooleanField(default=True, null=True, blank=True)
	is_nac = models.BooleanField(default=False, null=True, blank=True)
	is_mun = models.BooleanField(default=False, null=True, blank=True)
	is_post = models.BooleanField(default=False, null=True, blank=True)
	image = models.ImageField(upload_to='funsionariu', null=True,blank=True)
	tipu_f = models.CharField(choices=[('Chefe Suco','Chefe Suco'),('Chefe Aldeia','Chefe Aldeia')],max_length=30,null=True,blank=True)
	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)


	def __str__(self):
		template = '{0.naran} {0.pozisaun}'
		return template.format(self)

class UserFunsionariu(models.Model):
	user =  models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name="userFunsionariu")
	funsionariu = models.OneToOneField(Funsionariu,on_delete=models.CASCADE,related_name="userFunsionariu")
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)
	def __str__(self):
		template = '{0.funsionariu} {0.user}'
		return template.format(self)	


