#-*- encoding=utf-8 -*-

from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from django.forms.widgets import HiddenInput
from newspaper.models import News

class NewsForm(ModelForm):
	class Meta:
		model= News
		fields = '__all__'

class PartialNewsForm(ModelForm):
	class Meta:
		model= News
		exclude  = ['dating_news', 'comments']		
		widgets = {
			'author': HiddenInput(),
		}
	def setAuthor(self, author):
		data = self.data.copy()
		data['author'] = author
		self.data = data
