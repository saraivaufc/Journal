#-*- encoding=utf-8 -*-

from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Classifield
import hashlib


class ClassifieldForm(ModelForm):
	class Meta:
		model= Classifield
		fields = '__all__'

class PartialClassifieldForm(ModelForm):
	class Meta:
		model= Classifield
		exclude  = ['creator_classifield', 'offers']

	def clean_image(self):
		image = self.cleaned_data["image"]
		if image:
			hash = hashlib.md5(image.read()).hexdigest()
			image.name = "".join((hash, ".", image.name.split(".")[-1]))
		return image
