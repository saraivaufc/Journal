from django.db import models
from django.utils.translation import ugettext as _
from .userAutheticated import UserAutheticated

class Journalist(UserAutheticated):
	def registeringNews(self):
		pass
	def deleteNews(self):
		pass

	def __unicode__(self):
		return self.username

	class Meta:
		verbose_name = _("Journalist")
		verbose_name_plural = _("Journalists")

		permissions = (("registering_news", "Registering News"),
                       ("delete_news", "Delete News"),
                      )