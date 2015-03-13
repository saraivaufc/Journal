from rolepermissions.roles import AbstractUserRole

class Journalist(AbstractUserRole):
	available_permissions = {
        'create_news': True,
        'delete_news': True,
    }

class Lector(AbstractUserRole):
	available_permissions = {
        'create_lector': True,
        'create_comment': True,
        'create_offer_buy': True,
    }

class Redator(AbstractUserRole):
	available_permissions = {
        'create_journalist': True,
        'create_classifielf': True,
        'create_page': True,
        'delete_news': True,
    }
