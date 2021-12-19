from setuptools import setup


setup(name='iscraper-python',
	version='1.0.1',
	description='Official Python SDK to consume https://iscraper.io LinkedIn data APIs.',
	author='iScraper',
	author_email='sales@iscraper.io',
	url='https://github.com/iscraper-project/iscraper-python/',
	license='MIT',
	python_requires='>3.5.2',
	packages=[
		'iscraper'
	],
	install_requires=[
		'validators',
		'requests'
	]
)