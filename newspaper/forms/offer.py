#-*- encoding=utf-8 -*-

from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from django.forms.widgets import HiddenInput
from newspaper.models import Offer

class OfferForm(ModelForm):
	class Meta:
		model= Offer
		fields = '__all__'

class PartialOfferForm(ModelForm):
	class Meta:
		model= Offer
		fields  = ['value', 'details']
