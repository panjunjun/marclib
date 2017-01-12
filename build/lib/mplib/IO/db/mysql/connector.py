# coding: utf-8
# __author__: u"John"
from __future__ import unicode_literals
from mplib.common.settings import MYSQL_SETTINGS
import MySQLdb


def db_connect(settings=MYSQL_SETTINGS):
    connection = MySQLdb.Connect(**settings)
    return connection


def db_cursor(settings=MYSQL_SETTINGS):
    cursor = MySQLdb.Connect(**settings).cursor()
    return cursor


class MPMySQL(object):

    def __init__(self, settings=MYSQL_SETTINGS):
        self.settings = settings

    def query(self, sql, dict_cursor=True, fetchone=False):
        conn = MySQLdb.connect(**self.settings)
        if dict_cursor:
            cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        else:
            cursor = conn.cursor()
        cursor.execute(sql)
        try:
            if fetchone:
                ret = [cursor.fetchone()]
            else:
                ret = list(cursor.fetchall())
        except Exception as e:
            print u"error message:{0}".format(e)
            return False
        else:
            return ret
        finally:
            cursor.close()
            conn.close()

    def execute(self, sql):
        conn = MySQLdb.connect(**self.settings)
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print u"error message:{0}".format(e)
            return False
        else:
            return True
        finally:
            cursor.close()
            conn.close()

    def execute_many(self, sql, args):
        conn = MySQLdb.connect(**self.settings)
        cursor = conn.cursor()
        try:
            cursor.executemany(sql, args)
            conn.commit()
        except Exception as e:
            print u"error message:{0}".format(e)
            return False
        else:
            return True
        finally:
            cursor.close()
            conn.close()


if __name__ == "__main__":
    print MPMySQL().query("SELECT now() AS time;", fetchone=True)
    print MPMySQL().query("SELECT now() AS time;")
