from django.forms import ModelForm,  Textarea, SelectMultiple, TextInput,  NumberInput
from newspaper.models import SubSection
import hashlib


class SubSectionForm(ModelForm):
	class Meta:
		model= SubSection
		fields = '__all__'

class PartialSubSectionForm(ModelForm):
	class Meta:
		model= SubSection
		fields = '__all__'
		widgets = {
			'title': TextInput(attrs={'required': 'required'}),
			'sections':  SelectMultiple(attrs={'required': 'required'}),
		}