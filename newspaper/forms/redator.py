from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Redator

class RedatorForm(ModelForm):
	class Meta:
		model= Redator
		fields = '__all__'

class PartialRedatorForm(ModelForm):
	class Meta:
		model= Redator
		fields = ("first_name", "last_name", "email","username", "password")
