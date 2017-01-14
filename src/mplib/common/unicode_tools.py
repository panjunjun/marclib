# coding: utf-8
# __author__: u"John"
from __future__ import unicode_literals
import chardet


def smart_decode(obj):
    """
    处理中文编码，根据要求返回unicode
    :param obj:
    :return:
    """
    if isinstance(obj, int) or isinstance(obj, long) or isinstance(obj, float) or isinstance(obj, unicode):
        return obj
    elif isinstance(obj, str):
        try:
            return obj.decode("utf8")
        except UnicodeDecodeError:
            pass
        try:
            return obj.decode("gbk")
        except UnicodeDecodeError:
            pass
        try:
            return obj.decode("gb2312")
        except UnicodeDecodeError:
            pass
        try:
            return obj.decode(chardet.detect(obj).get("encoding"))
        except UnicodeDecodeError:
            return obj
    elif isinstance(obj, list):
        return [smart_decode(i) for i in obj]
    elif isinstance(obj, dict):
        return {smart_decode(k): smart_decode(v) for k, v in obj.iteritems()}
    elif isinstance(obj, tuple):
        return tuple([smart_decode(i) for i in obj])
    else:
        return obj


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


def to_unicode(obj):
    if isinstance(obj, unicode):
        return obj

    elif isinstance(obj, str):
        return smart_decode(obj)

    elif isinstance(obj, int):
        return unicode(obj)

    elif isinstance(obj, list):
        return [to_unicode(i) for i in obj]

    elif isinstance(obj, dict):
        return {to_unicode(k): to_unicode(v) for k, v in obj.iteritems()}

    elif isinstance(obj, tuple):
        return tuple([to_unicode(i) for i in obj])

    else:
        return obj

if __name__ == "__main__":
    test_objs = [
        3,
        3L,
        2.5,
        "it's a unicode",
        ["a", b"你好", b"世界"],
        {b"key1": b"value1", b"key2": "值2", "键3": b"value3", "key4": 5.3},
        ("tuple[0]", b"元组", "奇怪的编码".encode("gb2312"))
    ]
    for test_obj in test_objs:
        print smart_decode(test_obj)
