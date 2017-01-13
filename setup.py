# coding: utf-8
# __author__: u"John"
from __future__ import unicode_literals
from setuptools import setup, find_packages


setup(
    name="mplib",
    version="0.4.1",
    packages=find_packages("src".encode("utf8")),
    package_dir={"": "src".encode("utf8")},
    include_package_data=True,
)
