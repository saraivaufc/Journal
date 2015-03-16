from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Lector

class LectorForm(ModelForm):
	class Meta:
		model= Lector
		fields = '__all__'

class PartialLectorForm(ModelForm):
	class Meta:
		model= Lector
		fields = ("first_name", "last_name", "email","username", "password")
