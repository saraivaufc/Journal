#-*- encoding=utf-8 -*-

from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Journalist
import hashlib

class JournalistForm(ModelForm):
	class Meta:
		model= Journalist
		fields = '__all__'

class PartialJournalistForm(ModelForm):
	class Meta:
		model= Journalist
		fields = ("first_name", "last_name", "email","username", "password", "profile_image")

	def clean_profile_image(self):
		image = self.cleaned_data["profile_image"]
		try:
			if image:
				hash = hashlib.md5(image.read()).hexdigest()
				image.name = "".join((hash, ".", image.name.split(".")[-1]))
		except:
			pass
		return image
