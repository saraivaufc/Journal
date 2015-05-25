#-*- encoding=utf-8 -*-

from django.forms import ModelForm,TextInput, EmailInput, PasswordInput
from newspaper.models import UserAuthenticated
import hashlib

class UserAuthenticatedForm(ModelForm):
	class Meta:
		model= UserAuthenticated
		fields = '__all__'

class PartialUserAuthenticatedForm(ModelForm):
	class Meta:
		model= UserAuthenticated
		fields = ("first_name", "last_name", "email","username", "password", "profile_image")

		widgets = {
			'first_name': TextInput(attrs={'required': 'required'}),
			'last_name': TextInput(attrs={'required': 'required'}),
			'email': EmailInput(attrs={'required': 'required'}),
			'username': TextInput(attrs={'required': 'required'}),
			'password': PasswordInput(attrs={'required': 'required'}),
		}


	def clean_profile_image(self):
		image = self.cleaned_data["profile_image"]
		try:
			if image:
				hash = hashlib.md5(image.read()).hexdigest()
				image.name = "".join((hash, ".", image.name.split(".")[-1]))
		except:
			pass
		return image
