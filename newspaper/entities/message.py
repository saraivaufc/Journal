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

	JOURNALIST_NOT_FOUND = _("Journalist not found")

	
	#Section
	SECTION_SUCCESS_ADD = _("Section successfully added")
	SECTION_ERROR_ADD = _("Error adding section")
	
	SECTION_SUCCESS_EDIT = _("Section successfully edit")
	SECTION_ERROR_EDIT = _("Error edit section")
	
	SECTION_SUCCESS_REM = _("Section successfully removed")
	SECTION_ERROR_REM = _("Error remove section")

	SECTION_NOT_FOUND = _("Section not found")

	#Section
	SUBSECTION_SUCCESS_ADD = _("SubSection successfully added")
	SUBSECTION_ERROR_ADD = _("Error adding subsection")
	
	SUBSECTION_SUCCESS_EDIT = _("SubSection successfully edit")
	SUBSECTION_ERROR_EDIT = _("Error edit subsection")
	
	SUBSECTION_SUCCESS_REM = _("SubSection successfully removed")
	SUBSECTION_ERROR_REM = _("Error remove subsection")

	SUBSECTION_NOT_FOUND = _("SubSection not found")

	#Section
	CLASSIFIELD_SUCCESS_ADD = _("Classifield successfully added")
	CLASSIFIELD_ERROR_ADD = _("Error adding classifield")
	
	CLASSIFIELD_SUCCESS_EDIT = _("Classifield successfully edit")
	CLASSIFIELD_ERROR_EDIT = _("Error edit classifield")
	
	CLASSIFIELD_SUCCESS_REM = _("Classifield successfully removed")
	CLASSIFIELD_ERROR_REM = _("Error remove classifield")

	CLASSIFIELD_NOT_FOUND = _("Classifield not found")
	CLASSIFIELDS_NOT_FOUND = _("Classifields not found")

	
	



class Message():
	text = ''
	type_msg =None 
	def __init__(self, text, type_msg):
		self.text = str(text)
		self.type_msg = type_msg

	def type(self):
		return self.type_msg
