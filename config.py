# Default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = 'dced95d8411c4192adbe152975d38cbe'
	# Here you can list all the languages ​​that you want to use in your application
	LANGUAGES = {
		'en': 'English',
		'zh': 'Chinese',
		'de': 'German'
	}

class TestConfig(BaseConfig):
	DEBUG = True
	TESTING = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False