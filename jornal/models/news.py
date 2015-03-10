from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime

class News(models.Model):
	title = models.CharField(max_length=50, verbose_name=_("Title"), )
	subtitle = models.CharField(max_length=150, verbose_name=_("Subtitle"), null=False, blank=False, )
	text = models.TextField(verbose_name=_("Text"), )
	author = models.ForeignKey("jornal.User", verbose_name=_("Author"), on_delete=models.CASCADE, )
	dating_news = models.DateTimeField(default=datetime.now,verbose_name=_("Dating News"), )
	page = models.ForeignKey("jornal.Page", verbose_name=_("Page"), on_delete=models.CASCADE, )
	
    