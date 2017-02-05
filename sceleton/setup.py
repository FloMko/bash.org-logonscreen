try:
	from setuptools import setup
except :mportError:
	from distutils.core import setup
config = {
	'description': 'My Project',
	'author': 'FloMaster',
	'author_email': 'flomko.ru@gmail.com',
	'url': 'http://localhost',
	'version': '0.1',
	'name': 'bashlogon'
	}


setup(**config)
