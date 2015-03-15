from django.forms import ModelForm,  Textarea, Select, TextInput,  NumberInput
from newspaper.models import Comment

class CommentForm(ModelForm):
	class Meta:
		model= Comment
		fields = '__all__'

class PartialCommentForm(ModelForm):
	class Meta:
		model= Comment
		exclude  = ['author', 'dating_comment']
