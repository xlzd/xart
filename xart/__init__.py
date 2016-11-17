#!/usr/bin/env python
# coding: utf8

from __future__ import print_function, unicode_literals

import argparse
import random
import sys
from functools import wraps

import errors
from font import Font
from renderer import Renderer

__version__ = '0.1.0'


def _print_all_fonts():
    sys.stdout.write('xart : generate art ascii fonts.\n\n')
    fonts = Font.get_all_fonts()
    for idx, font_name in enumerate(fonts):
        sys.stdout.write('  {}. {}\n'.format(idx, font_name))
    sys.stdout.write('\nAll {} fonts.\n\n'.format(len(fonts)))


def exception_handler(function):
    @wraps(function)
    def _deco(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except errors.XArtBaseException as err:
            sys.stderr.write('xart error: ')
            sys.stderr.write(err.msg)
            sys.stderr.write('\n')

    return _deco


@exception_handler
def main():
    parser = argparse.ArgumentParser(description='xart : generate art ascii fonts.')
    parser.add_argument('-f', '--font', default='', help='font to render with, default random', metavar='FONT')
    parser.add_argument('-i', '--info', default=False, help='show information of given font', action='store_true')
    parser.add_argument('-l', '--list', default=False, help='list all supported fonts', action='store_true')
    args, text = parser.parse_known_args()
    text = ''.join(text)

    if args.list:
        return _print_all_fonts()
    elif args.info:
        return print(Font(args.font).info)

    if not args.font:
        args.font = random.choice(Font.get_all_fonts())
    if not text:
        text = 'xart'

    renderer = Renderer(Font(args.font))
    renderer.render(text)


if __name__ == '__main__':
    main()
