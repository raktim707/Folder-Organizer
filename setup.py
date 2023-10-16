from setuptools import setup, find_packages
setup(
   name='sortify',
   version='0.1',
   author='Ruhel Ahmed Raktim',
   author_email='raktimahmed2019@outlook.com',
   description='File organizing Command Line Tool',
   packages=find_packages(),
   scripts=['src/sortify/sortify.py'],
)