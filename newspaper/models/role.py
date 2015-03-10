from django.db import models
from django.utils.translation import ugettext as _

class Role(models.Model):
	username = models.ForeignKey("newspaper.User", verbose_name=_("Username"))
	role = models.CharField(max_length=20, verbose_name=_("Role"),)

	def __unicode__(self):
		return self.username

	class Meta:
		ordering = ['-username']
		verbose_name = _("Role")
		verbose_name_plural = _("Roles")