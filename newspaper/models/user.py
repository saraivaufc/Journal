from django.db import models
from django.utils.translation import ugettext as _

class User(models.Model):
	def seeManchetes(self):
		pass

	def seeClassifield(self):
		pass

	def seeNews(self):
		pass

	class Meta:
		verbose_name = _("User")
		verbose_name_plural = _("Users")
