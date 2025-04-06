from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import Group,User
from funsionariu.models import UserFunsionariu,Funsionariu
from django.contrib.auth.forms import UserCreationForm
from .models import AdminSuku
from .models import AdminSuku, Municipality, AdministrativePost, Village, Aldeia
from crispy_forms.layout import Layout, Fieldset, Row, Column, Field, Div, Submit, HTML
from crispy_forms.bootstrap import PrependedText, AppendedText

class AdminSukuRegistrationForm(forms.ModelForm):
    username = forms.CharField(required=True, label="Username")
    email = forms.EmailField(required=True, label="Email")
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text="Password must contain at least 8 characters."
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as before, for verification."
    )
    
    class Meta:
        model = AdminSuku
        fields = ['username', 'email', 'password1', 'password2', 'phone', 'municipality', 
                 'administrativepost', 'village', 'aldeia', 'groups']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Inisialisasi queryset untuk dependent fields
        self.fields['municipality'].queryset = Municipality.objects.all()
        self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
        self.fields['village'].queryset = Village.objects.none()
        self.fields['aldeia'].queryset = Aldeia.objects.none()
        self.fields['groups'].queryset = Group.objects.all()
        
        # Handle dependent fields jika data sudah ada
        if 'municipality' in self.data:
            try:
                municipality_id = int(self.data.get('municipality'))
                self.fields['administrativepost'].queryset = AdministrativePost.objects.filter(
                    municipality_id=municipality_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.municipality:
            self.fields['administrativepost'].queryset = self.instance.municipality.administrativepost_set.order_by('name')

        if 'administrativepost' in self.data:
            try:
                post_id = int(self.data.get('administrativepost'))
                self.fields['village'].queryset = Village.objects.filter(
                    administrativepost_id=post_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.administrativepost:
            self.fields['village'].queryset = self.instance.administrativepost.village_set.order_by('name')

        if 'village' in self.data:
            try:
                village_id = int(self.data.get('village'))
                self.fields['aldeia'].queryset = Aldeia.objects.filter(
                    village_id=village_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.village:
            self.fields['aldeia'].queryset = self.instance.village.aldeia_set.order_by('name')

        # Setup FormHelper
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        
        self.helper.layout = Layout(
            Fieldset(
                'Informasaun User',
                'username',
                Row(
                    Column('email', css_class='col-md-8'),
                    Column('phone', css_class='col-md-4'),
                ),
                Row(
                    Column('password1', css_class='col-md-6'),
                    Column('password2', css_class='col-md-6'),
                ),
            ),
            
            Fieldset(
                'Informasaun Lokalizasaun',
                Row(
                    Column('municipality', css_class='col-md-6'),
                    Column('administrativepost', css_class='col-md-6'),
                    Column('village', css_class='col-md-6'),
                    Column('aldeia', css_class='col-md-6'),
                ),
            ),
            
            Fieldset(
                'Priviléjiu no Grupu',
                Div(
                    Field('groups'),
                    css_class='border p-3 rounded mb-3'
                )
            ),
            
            Div(
                Submit('submit', 'Registra', css_class='btn btn-primary me-2'),
                HTML("""<a class="btn btn-secondary" onclick="window.history.back()">Kansela</a>"""),
                css_class='d-flex justify-content-end mt-4'
            )
        )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username ida ne'e ona uza iha sistema.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email ida ne'e ona uza iha sistema.")
        return email

    def save(self, commit=True):
        # Create User first
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
        )
        
        # Then create AdminSuku profile
        admin_suku = super().save(commit=False)
        admin_suku.user = user
        
        if commit:
            admin_suku.save()
            self.save_m2m()  # Save many-to-many relations (groups)
            
            # Add to Admin Suku group by default
            admin_group, _ = Group.objects.get_or_create(name='Admin Suku')
            user.groups.add(admin_group)
        
        return admin_suku


class DateInput(forms.DateInput):
	input_type = 'date'

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('username', css_class='form-group col-md-6 mb-0'),
				Column('email', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-primary" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Funsionariu
		fields = ['naran','seksu','email','nu_telefone']
		exclude = [
			'pozisaun','aldeia','village','administrativepost','municipality','tipu_f','areamunicipality','areaadministrativepost',\
			'areavillage','image','user_created','date_created','hashed'
		]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('naran', css_class='form-group col-md-6 mb-0'),
				Column('seksu', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('email', css_class='form-group col-md-4 mb-0'),
				Column('nu_telefone', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),

			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class PhotoProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Funsionariu
		fields = ['image']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('image', css_class='form-group col-md-6 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

