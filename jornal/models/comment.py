from django.db import models
from django.utils.translation import ugettext as _

class Comment(models.Model):
	news = models.ForeignKey("jornal.News", verbose_name=_("News"), on_delete=models.CASCADE, )
	author = models.ForeignKey("jornal.User", verbose_name=_("Author"), on_delete=models.CASCADE, )
	text = models.TextField(verbose_name=_("Text"),)
	