from setuptools import setup

setup(
	name = 'Booklover',
	version='0.1',
	description = 'A package for booklovers',
	url='https://github.com/melmoheb/h09package',
	author='Mohamad El Moheb',
	author_email='krb3ym@virginia.edu',
	license='LICENSE',
	packages=['booklover', 'booklover_test'],
    install_requires = ['pandas']
)
