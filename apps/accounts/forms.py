from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, get_user_model, login, logout	
from django.contrib import messages

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField(label='Nombre de usuario')
	password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		 
		if username and password:
			user_qs = User.objects.filter(username=username)
			user = authenticate(username=username, password=password)
			if user is None:
				raise forms.ValidationError("Usuario o contraseña incorrecta")
			# if not user.check_password(password):
			# 	raise forms.ValidationError("Incorrect password")
			if not  user.is_active:
				raise forms.ValidationError("El usuario no está activo")
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	username = forms.CharField(min_length=3, label='Nombre de usuario')
	email = forms.EmailField(label='Email')
	email2 = forms.EmailField(label='Confirme Email')
	password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
	password2 = forms.CharField(widget=forms.PasswordInput, label='Repetir Contraseña')
	
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email2',
			'password',
			'password2'		
		]
		help_texts = {
            'username': None,
        }

	def clean(self, *args, **kwargs):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError('Los Emails deben coincidir')
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("El Email ingresado ya se encuentra registrado")
		if password != password2:
			raise forms.ValidationError("Las contraseñas no coinciden")
		return super(UserRegisterForm, self).clean(*args, **kwargs)