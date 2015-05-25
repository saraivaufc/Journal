from .userAuthenticated import UserAuthenticatedForm, PartialUserAuthenticatedForm
from newspaper.models import Lector


class LectorForm(UserAuthenticatedForm):
	class Meta(UserAuthenticatedForm.Meta):
		model= Lector

class PartialLectorForm(PartialUserAuthenticatedForm):
	class Meta(PartialUserAuthenticatedForm.Meta):
		model= Lector