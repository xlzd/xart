#!/usr/bin/env python

from setuptools import setup


setup(
    name='xart',
    version='0.0.1',
    description='ASCII text by xlzd',
    license='WTFPL',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Hackers',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Fonts',
    ],
    author='xlzd',
    author_email='i@xlzd.me',
    url='https://github.com/xlzd/xart',
    packages=['xart', 'xart.fonts'],
    package_data={'xart.fonts': ['*.flf', '*.flc']},
    entry_points={
        'console_scripts': [
            'xart = xart:main',
        ],
    }
)
