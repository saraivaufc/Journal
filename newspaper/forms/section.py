from django.forms import ModelForm, TextInput
from newspaper.models import Section
import hashlib


class SectionForm(ModelForm):
	class Meta:
		model= Section
		fields = '__all__'

class PartialSectionForm(ModelForm):
	class Meta:
		model= Section
		fields = ['title', 'image']
		widgets = {
			'title': TextInput(attrs={'required': 'required'}),
		}
