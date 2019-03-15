# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup


setup(
    name="IBnator",
    version='0.0.1',
    provides=['IBnator'],
    author="bt3",
    setup_requires='setuptools',
    packages=find_packages(),
    install_requires=[
        "keyring==10.4.0",
        "duo-client",
        "slackclient==1.0.9"
    ],
    entry_points = {
        'console_scripts': ['IBnator=IBnator.IBnator:main'],
    },
)