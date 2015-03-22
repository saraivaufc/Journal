#-*- encoding=utf-8 -*-

from .userAuthenticated import UserAuthenticatedForm, PartialUserAuthenticatedForm
from newspaper.models import Journalist

class JournalistForm(UserAuthenticatedForm):
	class Meta(UserAuthenticatedForm.Meta):
		model= Journalist

class PartialJournalistForm(PartialUserAuthenticatedForm):
	class Meta(PartialUserAuthenticatedForm.Meta):
		model= Journalist
