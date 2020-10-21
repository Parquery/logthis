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
    version='1.0.1',
    description='a singleton, two-level, colorful, thread-safe, knob-free, logging library for in-house software',
    long_description=long_description,
    url='https://github.com/Parquery/logthis',
    author='Marko Ristin',
    author_email='marko.ristin@parquery.com',
    license='MIT License',
    classifiers=[
        # yapf: disable
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
        # yapf: enable
    ],
    keywords='logging log colorful color simple plain straightforward',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    extras_require={
        'dev': [
            # yapf: disable
            'mypy==0.790',
            'pylint==2.6.0',
            'yapf==0.20.2',
            'coverage>=5,<6',
            'pydocstyle>=5,<6',
            'tox>=3.0.0,<4',
            'temppathlib>=1.0.3,<2',
            'twine'
            # yapf: enable
        ]
    },
    py_modules=['logthis'],
    package_data={"logthis": ["py.typed"]})
