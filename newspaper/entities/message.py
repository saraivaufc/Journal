#-*- encoding=utf-8 -*-
from django.utils.translation import ugettext as _


class TypeMessage():
	SUCCESS = _('SUCCESS')
	INFO = _('INFO')
	WARNING = _('WARNING')
	ERROR = _('ERROR')

class TextMessage():
	
	#User
	USER_NOT_PERMISSION = _("User does not have permission")
	USER_NOT_FOUND = _("User not found")


	#Forms
	ERROR_FORM = _("There was an error on the form")

	#News
	NEWS_SUCCESS_ADD = _("News added successfully")
	NEWS_ERROR_ADD = _("Failed to add news")
	
	NEWS_SUCCESS_EDIT = _("Edited successfully news")
	NEWS_ERROR_EDIT = _("Failed to edit news")
	
	NEWS_SUCCESS_REM = _("Removed successfully News")
	NEWS_ERROR_REM = _("Failed to remove news")

	NEWS_NOT_FOUND = _("News not found")



	#Journalist
	JOURNALIST_SUCCESS_ADD = _("Journalist successfully added")
	JOURNALIST_ERROR_ADD = _("Error adding journalist")
	
	JOURNALIST_SUCCESS_EDIT = _("Journalist successfully edit")
	JOURNALIST_ERROR_EDIT = _("Error edit journalist")
	
	JOURNALIST_SUCCESS_REM = _("Journalist successfully removed")
	JOURNALIST_ERROR_REM = _("Error remove journalist")
	
	
	



class Message():
	text = ''
	type_msg =None 
	def __init__(self, text, type_msg):
		self.text = str(text)
		self.type_msg = type_msg

	def type(self):
		return self.type_msg
