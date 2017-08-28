#!/usr/bin/env python
# coding: utf-8

import codecs

import pypandoc

if __name__ == '__main__':
    README = pypandoc.convert('README.md', 'rst')
    with codecs.open('README.rst', 'wb', encoding='utf-8') as fp:
        fp.write(README)
