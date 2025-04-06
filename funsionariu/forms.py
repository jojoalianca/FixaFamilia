from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from .models import *
from custom.models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class FunsionariuForm(forms.ModelForm):
	class Meta:
		model = Funsionariu
		fields = ['image','naran','municipality','administrativepost','village','areamunicipality','areaadministrativepost','nu_telefone','email','seksu','pozisaun','tipu_f']
		exclude = ['user_created','hashed','date_created','aldeia','areavillage']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['tipu_f'].required = True
		self.fields['municipality'].queryset = Municipality.objects.all()
		self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
		self.fields['village'].queryset = Village.objects.none()
		self.fields['areamunicipality'].queryset = Municipality.objects.all()
		self.fields['areaadministrativepost'].queryset = AdministrativePost.objects.none()
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

		if 'areamunicipality' in self.data:
			try:
				areamunicipality = int(self.data.get('areamunicipality'))
				self.fields['areaadministrativepost'].queryset = AdministrativePost.objects.filter(municipality__id=areamunicipality).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['areaadministrativepost'].queryset = self.instance.areamunicipality.administrativepost_set.order_by('name')

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('municipality', css_class='form-group col-md-4 mb-0'),
				Column('administrativepost', css_class='form-group col-md-4 mb-0'),
				Column('village', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('naran', css_class='form-group col-md-4 mb-0'),
				Column('seksu', css_class='form-group col-md-4 mb-0'),
				Column('pozisaun', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('nu_telefone', css_class='form-group col-md-4 mb-0'),
				Column('email', css_class='form-group col-md-4 mb-0'),
				Column('tipu_f', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
	        HTML(""" 
	        	
	        	<script>
				  var $j = jQuery.noConflict();
				  $j("#id_tipu_f").change(function () {
				    var tipu_fId = $j(this).val();
				    console.log("koko"+tipu_fId);
				    $j.ajax({
				      url: "{% url 'ajax_load_work_area' %}",
				      data: {
				        'tipu_f': tipu_fId,
				      },
				      success: function (data) {
				        $j("#outputWorkArea").html(data);
				      }
				    });

				  });
				</script>
	        """),
	        HTML("""<hr>  <div id='outputWorkArea'> </div> <hr>"""),

			Row(
				Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
						css_class='form-row'
			),
	        HTML(""" <center> <img id='output' width='200' /> </center> """),

			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)


class UpdateFunsionariuForm(forms.ModelForm):
	class Meta:
		model = Funsionariu
		fields = ['image','naran','municipality','administrativepost','village','nu_telefone','email','seksu','pozisaun']
		exclude = ['user_created','hashed','date_created']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['municipality'].queryset = Municipality.objects.all()
		self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
		self.fields['village'].queryset = Village.objects.none()
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

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('municipality', css_class='form-group col-md-4 mb-0'),
				Column('administrativepost', css_class='form-group col-md-4 mb-0'),
				Column('village', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('naran', css_class='form-group col-md-4 mb-0'),
				Column('seksu', css_class='form-group col-md-4 mb-0'),
				Column('pozisaun', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('nu_telefone', css_class='form-group col-md-4 mb-0'),
				Column('email', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
						css_class='form-row'
			),
	        HTML(""" <center> <img id='output' width='200' /> </center> """),

			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

