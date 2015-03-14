from django.db import models
from django.utils.translation import ugettext as _
from .userAutheticated import UserAutheticated

class Redator(UserAutheticated):
	def registeringJournalist(self):
		pass

	def registeringPage(self):
		pass

	def registeringClassifield(self):
		pass

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	class Meta:
		verbose_name = _("Redator")
		verbose_name_plural = _("Redators")