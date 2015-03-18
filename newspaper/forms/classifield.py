#-*- encoding=utf-8 -*-

from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Classifield

class ClassifieldForm(ModelForm):
	class Meta:
		model= Classifield
		fields = '__all__'

class PartialClassifieldForm(ModelForm):
	class Meta:
		model= Classifield
		exclude  = ['creator_classifield', 'offers']
