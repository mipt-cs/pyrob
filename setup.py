#!/usr/bin/python3

from setuptools import setup


setup(
    name='pyrob',
    version='0.1',
    url='https://github.com/mipt-cs-on-python3/pyrob',
    license='MIT',
    author='Alexey Ermakov',
    author_email='ermakov.as@mipt.ru',
    packages=['pyrob', 'pyrob.tasks', 'pyrob.samples', 'pyrob.solutions'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
    ],
    test_suite='pyrob.tests',
)
