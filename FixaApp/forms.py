from django import forms
from crispy_forms.helper import FormHelper
from django.shortcuts import get_object_or_404
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from .models import *
from custom.models import *
from users.models import *
class DateInput(forms.DateInput):
	input_type = 'date'

class XefeFamilia_Form(forms.ModelForm): 
	class Meta:
		model = ChefeFamilia
		fields = ['image','municipality','administrativepost','village','tinan','nu_Fixa','xefe_Familia','aldeia',]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['municipality'].queryset = Municipality.objects.all()
		self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
		self.fields['village'].queryset = Village.objects.none()
		self.fields['aldeia'].queryset = Aldeia.objects.none()
		if 'municipality' in self.data:
			try:
				municipality = int(self.data.get('municipality'))
				self.fields['administrativepost'].queryset = AdministrativePost.objects.filter(municipality__id=municipality).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['administrativepost'].queryset = self.instance.municipality.administrativepost_set.order_by('name')

		if 'administrativepost' in self.data:
			try:
				administrativepost = int(self.data.get('administrativepost'))
				self.fields['village'].queryset = Village.objects.filter(administrativepost__id=administrativepost).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['village'].queryset = self.instance.administrativepost.village_set.order_by('name')

		if 'village' in self.data:
			try:
				village = int(self.data.get('village'))
				self.fields['aldeia'].queryset = Aldeia.objects.filter(village__id=village).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['aldeia'].queryset = self.instance.village.aldeia_set.order_by('name')

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('tinan', css_class='form-group col-md-4 mb-0'),
				Column('nu_Fixa', css_class='form-group col-md-4 mb-0'),
				Column('xefe_Familia', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
				),
			Row(
	
				Column('municipality', css_class='form-group col-md-3 mb-0'),
				Column('administrativepost', css_class='form-group col-md-3 mb-0'),
				Column('village', css_class='form-group col-md-3 mb-0'),
				Column('aldeia', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
				),
			
			Row(
				Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
				),
			HTML(""" <center> <img id='output' width='200' /> </center> """),
			HTML(
				""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
			HTML(
				"""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)

class ChefeFamiliaForm1(forms.ModelForm): 
    class Meta:
        model = ChefeFamilia
        fields = ['image', 'municipality', 'administrativepost', 'village', 'tinan', 'nu_Fixa', 'xefe_Familia', 'aldeia']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Ambil user jika ada
        super().__init__(*args, **kwargs)
        
        # Jika user adalah Admin Suku, filter berdasarkan wilayah mereka
        if user and user.groups.filter(name="Admin Suku").exists():
            admin_suku = get_object_or_404(AdminSuku, user=user)
            self.fields['municipality'].initial = admin_suku.municipality
            self.fields['administrativepost'].initial = admin_suku.administrativepost
            self.fields['village'].initial = admin_suku.village
            self.fields['aldeia'].queryset = Aldeia.objects.filter(village=admin_suku.village)
            
            # Nonaktifkan pilihan untuk munisipiu, postu, dan suku agar tidak bisa diubah
            self.fields['municipality'].disabled = True
            self.fields['administrativepost'].disabled = True
            self.fields['village'].disabled = True
        else:
            self.fields['municipality'].queryset = Municipality.objects.all()
            self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
            self.fields['village'].queryset = Village.objects.none()
            self.fields['aldeia'].queryset = Aldeia.objects.none()

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('tinan', css_class='form-group col-md-4 mb-0'),
                Column('nu_Fixa', css_class='form-group col-md-4 mb-0'),
                Column('xefe_Familia', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('municipality', css_class='form-group col-md-3 mb-0'),
                Column('administrativepost', css_class='form-group col-md-3 mb-0'),
                Column('village', css_class='form-group col-md-3 mb-0'),
                Column('aldeia', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
            ),
            HTML(""" <center> <img id='output' width='200' /> </center> """),
            HTML(
                """ <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
            HTML(
                """  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
        )


class membroFamiliaForm(forms.ModelForm):
	Data_moris = forms.DateField(label='Data Moris', widget=DateInput())
	class Meta:
		model = DetCidadaun
		fields = ['naran','seksu','municipality','administrativepost','village','aldeia','relasaun','Fatin_Moris','Data_Moris','EStadi_Civil','Profisaun','religiaun','habilitasaun','relasaun']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['municipality'].queryset = Municipality.objects.all()
		self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
		self.fields['village'].queryset = Village.objects.none()
		self.fields['aldeia'].queryset = Aldeia.objects.none()
		if 'municipality' in self.data:
			try:
				municipality = int(self.data.get('municipality'))
				self.fields['administrativepost'].queryset = AdministrativePost.objects.filter(municipality__id=municipality).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['administrativepost'].queryset = self.instance.municipality.administrativepost_set.order_by('name')

		if 'administrativepost' in self.data:
			try:
				administrativepost = int(self.data.get('administrativepost'))
				self.fields['village'].queryset = Village.objects.filter(administrativepost__id=administrativepost).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['village'].queryset = self.instance.administrativepost.village_set.order_by('name')

		if 'village' in self.data:
			try:
				village = int(self.data.get('village'))
				self.fields['aldeia'].queryset = Aldeia.objects.filter(village__id=village).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['aldeia'].queryset = self.instance.village.aldeia_set.order_by('name')

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
               
				Column('naran', css_class='form-group col-md-6 mb-0', ),
				Column('seksu', css_class='form-group col-md-6 mb-0',),
				Column('relasaun', css_class='form-group col-md-6 mb-0', ),
				Column('Fatin_Moris', css_class='form-group col-md-6 mb-0', ),
				Column('Data_moris', css_class='form-group col-md-6 mb-0', ),
				Column('EStadi_Civil', css_class='form-group col-md-6 mb-0',),
				Column('Profisaun', css_class='form-group col-md-6 mb-0', ),
				Column('religiaun', css_class='form-group col-md-6 mb-0', ),
				Column('habilitasaun', css_class='form-group col-md-6 mb-0', ),
                
            ),
            Row(
	
				Column('municipality', css_class='form-group col-md-3 mb-0'),
				Column('administrativepost', css_class='form-group col-md-3 mb-0'),
				Column('village', css_class='form-group col-md-3 mb-0'),
				Column('aldeia', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
				),
            
			HTML(
				""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
			HTML(
				"""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
        )