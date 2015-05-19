from django.http import HttpResponseRedirect, HttpResponse
import time
from django.utils.translation import ugettext as _

def dateTimeNow(request):
	return HttpResponse(str(time.asctime(time.localtime(time.time()))))

