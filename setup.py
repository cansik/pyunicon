from distutils.core import setup

setup(
    name='pyunicon',
    version='1.0',
    packages=['tests', 'pyunicon', 'pyunicon.X11', 'pyunicon.util', 'pyunicon.Cocoa', 'pyunicon.WinForm'],
    url='https://github.com/cansik/pyunicon',
    license='The MIT License (MIT)',
    author='Florian Bruggisser',
    author_email='florian@nexpose.ch',
    description='PyUnicon is a cross platform library to control keyboard and mouse.'
)