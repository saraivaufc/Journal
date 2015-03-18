#-*- encoding=utf-8 -*-

from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Journalist

class JournalistForm(ModelForm):
	class Meta:
		model= Journalist
		fields = '__all__'

class PartialJournalistForm(ModelForm):
	class Meta:
		model= Journalist
		fields = ("first_name", "last_name", "email","username", "password", "profile_image")
