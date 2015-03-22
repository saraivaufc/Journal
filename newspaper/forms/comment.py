#-*- encoding=utf-8 -*-

from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Comment
import hashlib

class CommentForm(ModelForm):
	class Meta:
		model= Comment
		fields = '__all__'

class PartialCommentForm(ModelForm):
	class Meta:
		model= Comment
		exclude  = [ 'author','dating_comment']

	def clean_image(self):
		image = self.cleaned_data["image"]
		try:
			if image:
				hash = hashlib.md5(image.read()).hexdigest()
				image.name = "".join((hash, ".", image.name.split(".")[-1]))
		except:
			pass
		return image
