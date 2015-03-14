from django.db import models
from django.utils.translation import ugettext as _
from .userAutheticated import UserAutheticated

class Lector(UserAutheticated):
	def commentNews(self):
		pass

	def addOffer(self):
		pass

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	class Meta:
		verbose_name = _("Lector")
		verbose_name_plural = _("Lectors")