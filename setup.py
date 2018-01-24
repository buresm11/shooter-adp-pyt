from setuptools import setup

setup(
	name='shooter',
	version='0.1',
	description='Shooting game',
	author='Michal Bures',
	author_email="buresm11@fit.cvut.cz",
	keywords='game, shooting',
	license='Public domain',
	url='https://gist.github.com/oskar456/e91ef3ff77476b0dbc4ac19875d0555e',
	packages=['shooter'],
	classifiers=[
    	'License :: Public Domain',
    	'Programming Language :: Python',
    	'Topic :: Games/Entertainment'],
    zip_safe=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    install_requires=['pyglet']
)