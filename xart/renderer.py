#!/usr/bin/env python
# coding: utf8

from __future__ import unicode_literals


class Renderer(object):
    def __init__(self, font):
        self.font = font

    def render(self, text):
        data = [[] for _ in xrange(self.font.height)]
        for ch in text:
            for idx, line in enumerate(self.font.getchar(ch)['char']):
                data[idx].append(line)
        return '\n'.join(''.join(item) for item in data)
