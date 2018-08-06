"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
import os

from setuptools import setup, find_packages

# pylint: disable=redefined-builtin

here = os.path.abspath(os.path.dirname(__file__))  # pylint: disable=invalid-name

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()  # pylint: disable=invalid-name

setup(
    name='logthis',
    version='1.0.0',
    description='a singleton, two-level, colorful, thread-safe, knob-free, logging library for in-house software',
    long_description=long_description,
    url='https://bitbucket.org/parqueryopen/logthis',
    author='Marko Ristin',
    author_email='marko.ristin@parquery.com',
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='logging log colorful color simple plain straightforward',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    extras_require={
        'dev': ['mypy==0.600', 'pylint==1.8.4', 'yapf==0.20.2', 'tox>=3.0.0', 'temppathlib==1.0.1'],
        'test': ['tox==3.0.0', 'temppathlib==1.0.1']
    },
    py_modules=['logthis'])
