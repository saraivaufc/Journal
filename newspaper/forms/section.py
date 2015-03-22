from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Section
import hashlib


class SectionForm(ModelForm):
	class Meta:
		model= Section
		fields = '__all__'

class PartialSectionForm(ModelForm):
	class Meta:
		model= Section

	def clean_image(self):
		image = self.cleaned_data["image"]
		try:
			if image:
				hash = hashlib.md5(image.read()).hexdigest()
				image.name = "".join((hash, ".", image.name.split(".")[-1]))
		except:
			pass
		return image
