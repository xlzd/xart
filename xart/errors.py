#!/usr/bin/env python
# coding: utf8

from __future__ import unicode_literals


class XArtBaseException(Exception):
    def __init__(self, message):
        super(XArtBaseException, self).__init__()
        if not isinstance(message, unicode):
            message = message.decode("utf-8")
        self._message = message

    def __str__(self):
        return '{0}: message={1}.'.format(self.__class__.__name__, self._message.encode("utf8"))

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return '{0}: message={1}.'.format(self.__class__.__name__, self._message)

    @property
    def msg(self):
        return self._message


class FontNotExist(XArtBaseException):
    pass


class InvalidFont(XArtBaseException):
    pass


class ColorError(XArtBaseException):
    pass
