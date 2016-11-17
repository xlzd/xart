#!/usr/bin/env python
# coding: utf8

from __future__ import unicode_literals

import os
import re

import errors


class Font(object):
    HEADER_PATTERN = re.compile(r'^[tf]lf2.')
    END_PATTERN = re.compile(r'(.)\s*$')

    def __init__(self, font_name):
        self._font_name = font_name
        self._comment = ''
        self._height = -1
        self._data = {}
        self._suffix = None
        self._hard_blank = None
        self.init()

    @classmethod
    def get_all_fonts(cls):
        path = os.path.join(os.path.dirname(__file__), 'fonts')
        return [font.rsplit('.', 1)[0] for font in os.listdir(path)]

    def _load_raw_data(self):
        path = os.path.join(os.path.dirname(__file__), 'fonts', self._font_name)

        for ext in ('.flf', '.tlf'):
            if os.path.exists(path + ext):
                with open(path + ext, 'r') as fp:
                    return fp.read().decode('utf-8', 'ignore')
        raise errors.FontNotExist('Font <{}> not found'.format(self._font_name))

    def _parse_header(self, header):
        if self.HEADER_PATTERN.search(header) is None:
            raise errors.InvalidFont('Font <{}> error'.format(self._font_name))
        header = self.HEADER_PATTERN.sub('', header).split()
        if len(header) < 6:
            raise errors.InvalidFont('Font <{}> error'.format(self._font_name))
        self._hard_blank = header[0]
        self._height, _, _, _, self._comment_lines = map(int, header[1:6])

    def _build_char(self, data):
        chars = []
        for pos in xrange(self.height):
            line = data.pop(0)
            if self._suffix is None:
                self._suffix = self.END_PATTERN.search(line).group(1)
                self._suffix = re.compile(re.escape(self._suffix) + r'{1,2}$')
            chars.append(self._suffix.sub('', line).replace(self._hard_blank, ' '))
        return chars, max(len(x) for x in chars)

    def init(self):
        data = self._load_raw_data().splitlines()
        self._parse_header(data.pop(0))
        self._comment = '\n'.join(data[:self._comment_lines])
        for _ in xrange(self._comment_lines):
            data.pop(0)

        for ch in xrange(32, 127):
            chars, width = self._build_char(data)
            self._data[ch] = {'char': chars, 'width': width}

        while data:
            line = data.pop(0).strip()
            i = line.split(' ', 1)[0]
            if i == '':
                continue
            hex_match = re.search('^0x', i, re.IGNORECASE)
            if hex_match is not None:
                i = int(i, 16)
                char, width = self._build_char(data)
                if ''.join(char) != '':
                    self._data[i] = {'char': char, 'width': width}

    @property
    def info(self):
        return self._comment

    @property
    def height(self):
        return self._height

    def getchar(self, char):
        return self._data[ord(char)]

    def __str__(self):
        return '<{} object: {}>'.format(self.__class__.__name__, self._font_name)
