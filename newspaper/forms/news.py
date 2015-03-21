#-*- encoding=utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from django.forms.widgets import HiddenInput
from newspaper.models import News
import hashlib


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

	def clean_image(self):

		image = self.cleaned_data["image"]
		if image:
			hash = hashlib.md5(image.read()).hexdigest()
			image.name = "".join((hash, ".", image.name.split(".")[-1]))
		return image

	def clean_video(self):
		video = self.cleaned_data["video"]
		if video:
			hash = hashlib.md5(video.read()).hexdigest()
			video.name = "".join((hash, ".", video.name.split(".")[-1]))
		return video


	def updateNameImage(self):
		pass
