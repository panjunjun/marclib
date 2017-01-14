# coding: utf-8
# __author__: u"John"
from __future__ import unicode_literals


def fib(index):
    """
    斐波那契数列
    :param index: 需要index位的数字 a[1] ... a[index]
    :return:
    """
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


if __name__ == "__main__":
    fibonacci = fib(6)
    print type(fibonacci)
    for i in fibonacci:
        print i
