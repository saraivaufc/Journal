from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import SubSection

class SubSectionForm(ModelForm):
	class Meta:
		model= SubSection
		fields = '__all__'

class PartialSubSectionForm(ModelForm):
	class Meta:
		model= SubSection
