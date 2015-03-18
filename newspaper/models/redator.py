from django.db import models
from django.utils.translation import ugettext as _
from .userAuthenticated import UserAuthenticated
from newspaper.models import Journalist

class Redator(UserAuthenticated):
	def registeringJournalist(self, form):
		if form.is_valid():
			form.save()
			return True
		else:
			return False

	def editJournalist(self,form):
		if form.is_valid():
			form.save()
			return True
		else:
			return False
	def remJournalist(self, id):
		try:
			Journalist.objects.get(id = id).delete()
			return True
		except:
			print "Falah ao remover Journalist"
			return False


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