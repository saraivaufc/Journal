from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Lector
import hashlib


class LectorForm(ModelForm):
	class Meta:
		model= Lector
		fields = '__all__'

class PartialLectorForm(ModelForm):
	class Meta:
		model= Lector
		fields = ("first_name", "last_name", "email","username", "password")

	def clean_profile_image(self):
		image = self.cleaned_data["profile_image"]
		try:
			if image:
				hash = hashlib.md5(image.read()).hexdigest()
				image.name = "".join((hash, ".", image.name.split(".")[-1]))
		except:
			pass
		return image
