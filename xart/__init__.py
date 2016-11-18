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

__version__ = '0.1.8'


def _print_version():
    sys.stdout.write('xart : generate art ascii fonts, version {}.\n'.format(__version__))
    _render_fonts(__version__)


def _print_all_fonts():
    output = ['xart : generate art ascii texts.\n']
    fonts = Font.get_all_fonts()
    for idx, font_name in enumerate(fonts):
        output.append('  {}. {}'.format(idx, font_name))
    output.append('\nAll {} fonts.\n'.format(len(fonts)))
    sys.stdout.write('\n'.join(output))


def exception_handler(function):
    @wraps(function)
    def _deco(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except errors.XArtBaseException as err:
            sys.stderr.write('xart error: {}\n'.format(err.msg))

    return _deco


def _render_fonts(text, font=None, show=False):
    if not font:
        font = random.choice(Font.get_all_fonts())
    if not text:
        text = 'xart'
    renderer = Renderer(Font(font))
    sys.stdout.write(renderer.render(text))
    if show:
        sys.stdout.write('Font name : {}\n'.format(font))


@exception_handler
def main():
    parser = argparse.ArgumentParser(description='xart : generate art ascii texts.')
    parser.add_argument('-f', '--font', default='', help='font to render with, default random', metavar='FONT')
    parser.add_argument('-i', '--info', default=False, help='show information of given font', action='store_true')
    parser.add_argument('-s', '--show', default=False, help='show random fonts', action='store_true')
    parser.add_argument('-l', '--list', default=False, help='list all supported fonts', action='store_true')
    parser.add_argument('-v', '--version', default=False, help='version', action='store_true')
    args, text = parser.parse_known_args()
    text = ''.join(text)

    if args.version:
        return _print_version()
    elif args.list:
        return _print_all_fonts()
    elif args.info:
        return print(Font(args.font).info)
    _render_fonts(text, args.font, args.show)


if __name__ == '__main__':
    main()
