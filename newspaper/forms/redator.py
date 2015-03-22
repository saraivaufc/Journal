from .userAuthenticated import UserAuthenticatedForm, PartialUserAuthenticatedForm
from newspaper.models import Redator

class RedatorForm(UserAuthenticatedForm):
	class Meta(UserAuthenticatedForm.Meta):
		model= Redator

class PartialRedatorForm(PartialUserAuthenticatedForm):
	class Meta(PartialUserAuthenticatedForm.Meta):
		model= Redator