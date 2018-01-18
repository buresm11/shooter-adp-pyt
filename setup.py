from setuptools import setup

setup(
	name='shooter',
	version='0.1',
	description='Shooting game',
	author='Michal Bures',
	author_email="buresm11@fit.cvut.cz",
	keywords='game, shooting',
	license='Public domain',
	packages=['shooter'],
	classifiers=[
		'Intended Audience :: Gamers',
    	'License :: Public Domain',
    	'Programming Language :: Python'],
    install_requires=['pyglet'],
    zip_safe=False
)