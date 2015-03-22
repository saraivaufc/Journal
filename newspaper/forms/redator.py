from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Redator
import hashlib

class RedatorForm(ModelForm):
	class Meta:
		model= Redator
		fields = '__all__'

class PartialRedatorForm(ModelForm):
	class Meta:
		model= Redator
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
