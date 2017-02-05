try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
config = {
	'description': 'My Project',
	'author': 'FloMaster',
	'url': 'http://localhost',
	'version': '0.1',
	'name': 'bashlogon'
	}


setup(**config)
