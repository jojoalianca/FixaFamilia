from django.db import models

# Create your models here.

class Municipality(models.Model):
	code = models.CharField(max_length=5, null=True, blank = True)
	name = models.CharField(max_length=100)
	hckey = models.CharField(max_length=32, null=True ,  blank = True)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class AdministrativePost(models.Model):
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class Village(models.Model):
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)

class Aldeia(models.Model):
	village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100)
	def __str__(self):
		template = '{0.name}'
		return template.format(self)


        
# class AcademicLevel(models.Model):
# 	name = models.CharField(max_length=50, verbose_name="Naran")
# 	def __str__(self):
# 		template = '{0.name}'
# 		return template.format(self)

# class Religion(models.Model):
#     name = models.CharField(max_length = 50,verbose_name='Relijiun')
#     def __str__(self):
#         template = '{0.name}'
#         return template.format(self)

#     class Meta:
#         verbose_name_plural='Dadus Custom Ba Relijiaun'
