# coding: utf-8
# __author__: u"John"
from __future__ import unicode_literals
import chardet


def smart_decode(string):
    """
    处理中文编码，根据要求返回unicode
    :param string:
    :return:
    """
    if isinstance(string, int) or isinstance(string, long) or isinstance(string, float) or isinstance(string, unicode):
        return string
    elif isinstance(string, str):
        try:
            return string.decode("utf8")
        except UnicodeDecodeError:
            pass
        try:
            return string.decode("gbk")
        except UnicodeDecodeError:
            pass
        try:
            return string.decode("gb2312")
        except UnicodeDecodeError:
            pass
        try:
            return string.decode(chardet.detect(string).get("encoding"))
        except UnicodeDecodeError:
            return string
    else:
        return string


def smart_encode(string, charset="utf8"):
    """
    处理Unicode编码，根据需求返回str
    :param string:
    :param charset:
    :return:
    """
    try:
        return string.encode(charset)
    except UnicodeEncodeError:
        return string


def change_charset(string, from_charset="utf8", to_charset="utf8"):
    if isinstance(string, unicode):
        return string.encode(to_charset)

    elif isinstance(string, str):
        try:
            return string.decode(from_charset).encode(to_charset)
        except UnicodeDecodeError:
            return string
        except UnicodeEncodeError:
            return string

    else:
        return string


def to_unicode(string, from_charset="utf8"):
    if isinstance(string, unicode):
        return string

    elif isinstance(string, str):
        return string.decode(from_charset)

    elif isinstance(string, int):
        return unicode(string)

    else:
        return string
