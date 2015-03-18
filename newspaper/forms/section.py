from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Section

class SectionForm(ModelForm):
	class Meta:
		model= Section
		fields = '__all__'

class PartialSectionForm(ModelForm):
	class Meta:
		model= Section
