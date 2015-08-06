from distutils.core import setup

from setuptools import find_packages


setup(
    name='stepic_search',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/taery/stepic_search',
    license='',
    author='Anastasia Lavrenko',
    author_email='lavrenko.a@gmail.com',
    install_requires=[
        "Django == 1.8.3",
        "elasticutils == 0.10.3",
        "requests == 2.7.0",
        "djangorestframework == 3.1.3",
    ]
)
