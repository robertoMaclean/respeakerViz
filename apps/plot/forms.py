from django import forms
from .models import UserFile

class FileForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(FileForm, self).__init__(*args, **kwargs)

	name = forms.CharField(min_length=3, label='Nombre', widget=forms.TextInput(attrs={'placeholder':'Ingresa el nombre del grupo'}))
	file = forms.FileField(label='Subir archivo')
	class Meta:
		model = UserFile
		fields = [
			'name',
			'file'
		]

	def clean_name(self):
		name = self.cleaned_data.get('name')
		name_objs = UserFile.objects.filter(user= self.request.user)
		name_qs = name_objs.filter(name = name)
		if name_qs.count() > 0:
			raise forms.ValidationError("El nombre ya existe")
		return name

	def clean_file(self):
		file = self.cleaned_data.get('file')
		file.chunks(4)
		max_size = 10000000
		print(file.size)
		if not file.name.endswith('.csv'):
			raise forms.ValidationError("El archivo no tiene extensión CSV")
		#if file.multiple_chunks():
		if file.size > max_size:
			raise forms.ValidationError("El archivo es muy grande (%.2f MB)." % (file.size/(1000*1000),))
		return file