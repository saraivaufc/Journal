#-*- encoding=utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from .userAuthenticated import UserAuthenticated

class Lector(UserAuthenticated):
	def commentNews(self, news, lector, text, image=''):
		try:
			from .comment import Comment
			c = Comment(author = lector, text= text, image = image)
			c.save()
			news.comments.add(c)
			print "Comment add sucess"
			return True
		except:
		 	print "Fail add Comment"
		 	return False

	def addOffer(self):
		pass

	def __unicode__(self):
		return self.username

	class Meta:
		verbose_name = _("Lector")
		verbose_name_plural = _("Lectors")
		permissions = (("registering_lector", "Registering Lector"),
                       ("comment_news", "Comment News"),
                       ("offer_to_buy", "Offer to Buy"),
                      )