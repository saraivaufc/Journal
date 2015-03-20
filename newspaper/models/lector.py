#-*- encoding=utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from .userAuthenticated import UserAuthenticated
from django.contrib.auth.models import Group, Permission


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

	def addOffer(self, classifield_id, form):
		from newspaper.models import Classifield, Comment, Offer
		try:
			classifield = Classifield.objects.get(id = classifield_id)
		except:
			return False
		if form.is_valid():
			try:
				value = form.cleaned_data['value']
				phone = form.cleaned_data['phone']
				if value > classifield.price and value > classifield.getBestOffer().value:
					details = form.cleaned_data['details']

					offer = Offer(author_offer_id = self.id,
								  value = value,
								  phone = phone,
								  details = details,)
					offer.save()
					classifield.offers.add(offer)
					return True
				else:
					return False
			except:
				print "Erro ao adicionar oferta"
				return False
		

	def registeringLector(self, form):
		if form.is_valid():
			form.save()
			try:
				u = Lector.objects.get(username = request.POST['username'])
				permission1 = Permission.objects.get(codename='registering_lector')
				permission2 = Permission.objects.get(codename='comment_news')
				permission3 = Permission.objects.get(codename='offer_to_buy')
				u.user_permissions.add(permission1, permission2, permission3)
			except:
				return False
		else:
			return False

	def __unicode__(self):
		return self.first_name + " " + self.last_name

	class Meta:
		verbose_name = _("Lector")
		verbose_name_plural = _("Lectors")
		permissions = (("registering_lector", "Registering Lector"),
                       ("comment_news", "Comment News"),
                       ("offer_to_buy", "Offer to Buy"),
                      )