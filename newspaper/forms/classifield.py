#-*- encoding=utf-8 -*-

from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Classifield
import hashlib
from django import forms

class ClassifieldForm(ModelForm):
	class Meta:
		model= Classifield
		fields = '__all__'

class PartialClassifieldForm(ModelForm):
	class Meta:
		model= Classifield
		fields  = ['title', 'description', 'price', 'phone', 'image']

		widgets = {
			'title': TextInput(attrs={'required': 'required'}),
			'description': Textarea(attrs={'required': 'required'}),
			'price': NumberInput(attrs={'required': 'required'}),
			'phone' : TextInput(),
		}
	def __init__(self, *args, **kwargs):
		super(PartialClassifieldForm, self).__init__(*args, **kwargs)
		self.fields['description'].widget.attrs['class'] = 'ckeditor'

	def clean_image(self):
		image = self.cleaned_data["image"]
		try:
			if image:
				hash = hashlib.md5(image.read()).hexdigest()
				image.name = "".join((hash, ".", image.name.split(".")[-1]))
		except:
			pass
		return image
