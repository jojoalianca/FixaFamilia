from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.db.models import Q
from .models import *

class MunisipiuForm(forms.ModelForm):
	class Meta:
		model = Municipality
		fields = ['name']
		labels = {
			"name":"Naran Munisipiu"
		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('name', css_class='form-group col-md-12 mb-0'),
			),
			HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
			HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)

class PostuForm(forms.ModelForm):
	class Meta:
		model = AdministrativePost
		fields = ['name','municipality']
		labels = {
			"municipality":"Naran Munisipiu",
			"name":"Naran Postu Administrativu"
		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('municipality', css_class='form-group col-md-6 mb-0'),
			),
			Row(
				Column('name', css_class='form-group col-md-6 mb-0'),
			),
			HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
			HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)

class SukuForm(forms.ModelForm):
	class Meta:
		model = Village
		fields = ['name','administrativepost']
		labels = {
			"administrativepost":"Naran Postu Administrativu",
			"name":"Naran Suku"
		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('administrativepost', css_class='form-group col-md-6 mb-0'),
			),
			Row(
				Column('name', css_class='form-group col-md-6 mb-0'),
			),
			HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
			HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)

class AldeiaForm1(forms.ModelForm):
	class Meta:
		model = Aldeia
		fields = ['village','name']
		labels = {
			"village":"Suku",
			"name":"Naran Aldeia"
		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('village', css_class='form-group col-md-6 mb-0'),
			),
			Row(
				Column('name', css_class='form-group col-md-6 mb-0'),
			),
			HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
			HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)

