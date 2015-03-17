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
		return self.username

	class Meta:
		verbose_name = _("Redator")
		verbose_name_plural = _("Redators")
		permissions = (("keep_journalist", "Keep Journalist"),
                       ("keep_classifield", "Keep Classifield"),
                       ("keep_section", "Keep Section"),
                       ("keep_subsection", "Keep SubSection"),
                       ("delete_news", "Delete News"),
                       ("access_manager", "Access Manager"),
                      )