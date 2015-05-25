from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from models import News

class NewsLatests(Feed):
	title = _('Latest News Published in The UFC Times')
	link = '/newspaper/'
	description = _("The UFC is reported here!")

	def items(self):
		return News.objects.order_by('-pub_date')[:5]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.description

	# item_link is only needed if NewsItem has no get_absolute_url method.
	def item_link(self, item):
		return reverse('news-item', args=[item.pk])

	def items(self):
		return News.objects.all()

	def item_link(self, news):
		return '/newspaper/news/%d/'%news.id