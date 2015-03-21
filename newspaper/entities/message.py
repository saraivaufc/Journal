#-*- encoding=utf-8 -*-

class TypeMessage():
	SUCCESS = 'SUCCESS'
	INFO = 'INFO'
	WARNING = 'WARNING'
	ERROR = 'ERROR'


class Message():
	text = ''
	type_msg =None 
	def __init__(self, text, type_msg):
		self.text = text
		self.type_msg = type_msg

	def type(self):
		return self.type_msg
