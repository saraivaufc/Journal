from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import SubSection
import hashlib


class SubSectionForm(ModelForm):
	class Meta:
		model= SubSection
		fields = '__all__'

class PartialSubSectionForm(ModelForm):
	class Meta:
		model= SubSection

	def clean_image(self):
		image = self.cleaned_data["image"]
		if image:
			hash = hashlib.md5(image.read()).hexdigest()
			image.name = "".join((hash, ".", image.name.split(".")[-1]))
		return image