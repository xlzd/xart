#!/usr/bin/env python
# coding: utf8

from __future__ import unicode_literals, print_function

from errors import ColorError

_FMT = u'\033[0;3{}m{}\033[0m'.format


class Color(object):
    COLORS = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'PURPLE', 'CYAN', 'GRAY', 'WHITE']
    # BLACK  = 0  # 黑
    # RED    = 1  # 红
    # GREEN  = 2  # 绿
    # YELLOW = 3  # 棕
    # BLUE   = 4  # 蓝
    # PURPLE = 5  # 紫
    # CYAN   = 6  # 青
    # GRAY   = 7  # 灰
    # WHITE  = 8  # 白

    @classmethod
    def all_colors(cls):
        return cls.COLORS

    @classmethod
    def get_color(cls, color):
        if color in cls.COLORS:
            return cls.COLORS.index(color)
        raise ColorError('color <{}> not found.'.format(color))

    @classmethod
    def dyeing(cls, string, color):
        if not isinstance(string, basestring):
            raise ValueError('string must be a str or unicode, got %s' % type(string))
        if isinstance(string, str):
            string = string.decode('utf-8')
        return _FMT(color, string)


class Renderer(object):
    # WIDTH = int(os.popen('stty size', 'r').read().split()[-1])

    def __init__(self, font):
        self.font = font

    def render(self, text):
        data = [[] for _ in xrange(self.font.height)]
        for ch in text:
            for idx, line in enumerate(self.font.getchar(ch)['char']):
                data[idx].append(line)
        return '\n'.join(''.join(item) for item in data) + '\n'
