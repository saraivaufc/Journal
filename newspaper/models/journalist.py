from django.db import models
from django.utils.translation import ugettext as _
from .userAuthenticated import UserAuthenticated

class Journalist(UserAuthenticated):
	def registeringNews(self, form):
		print form.fields['author'], self.id 
		form.setAuthor(self.id)
		if form.is_valid():
			form.save()
			print _("Added news with success")
		else:
			print _("Failed to add news")
	
	def deleteNews(self):
		pass

	def __unicode__(self):
		return self.username

	class Meta:
		verbose_name = _("Journalist")
		verbose_name_plural = _("Journalists")

		permissions = (("keep_news", "Keep News"),
					   ("access_manager", "Access Manager"),
                      )