# coding: utf-8
# __author__: u"John"
from __future__ import unicode_literals


MYSQL_SETTINGS = dict(
    host="172.16.1.120",
    port=3306,
    user="test",
    passwd="Marcpoint_2016",
    db="mp_portal",
)


HIVE_CONNECTION = dict(
    database="elengjing",
    host="192.168.110.122",
    user="hive",
    password="hive1",
    port=10000,
    authMechanism="PLAIN"
)


REDIS_CONNECTION = dict(
    host="localhost",
    port=6379
)


PG_CONNECTION = dict(
    host="192.168.110.11",
    port=5432,
    user="zsj",
    password="111111",
    dbname="mp_portal",
    minconn=1,
    maxconn=1000,
)


DEBUG = True
INFO = True
WARNING = True
ERROR = True
FATAL = True
