# coding: utf-8
# __author__: "John"
from __future__ import unicode_literals
from mplib.common.settings import PG_CONNECTION
import psycopg2.extras
import psycopg2.pool
import traceback
import psycopg2


class DatabaseSingleton(object):
    def __new__(cls, settings=PG_CONNECTION):
        if not hasattr(cls, "_instance"):
            orig = super(DatabaseSingleton, cls)
            cls._instance = orig.__new__(cls, settings)

            minconn = PG_CONNECTION.get("minconn")
            maxconn = PG_CONNECTION.get("maxconn")

            dsn = "host={host} port={port} dbname={dbname} user={user} password={password}".format(**settings)
            cls._instance.dbpool = psycopg2.pool.SimpleConnectionPool(minconn, maxconn, dsn=dsn)

        return cls._instance

    def __del__(self):
        self.dbpool.closeall()
        object.__del__(self)


class MPPG(DatabaseSingleton):
    def __init__(self):
        self.in_transaction = False

    def execute(self, operation, parameters=None):
        try:
            if not self.in_transaction:
                self.begin()
            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            if parameters:
                cursor.execute(operation, parameters)
            else:
                cursor.execute(operation)

            self.commit()
            cursor.close()

        except:
            traceback.print_exc()
            cursor.close()
            self.rollback()
            return False
        else:
            return True

    def execute1(self, operation, parameters=None):
        try:
            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            if parameters:
                cursor.execute(operation, parameters)
            else:
                cursor.execute(operation)
        except Exception, ex:
            print ex
            rowcount = cursor.rowcount
            cursor.close()
            return rowcount
        else:
            rowcount = cursor.rowcount
            cursor.close()
            return rowcount

    def executemany(self, operation, parameters=None):
        try:
            if not self.in_transaction:
                self.begin()
            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            if parameters:
                cursor.executemany(operation, parameters)
            else:
                cursor.executemany(operation)

            self.commit()

        except Exception, ex:
            print ex
            traceback.print_exc()
            cursor.close()
            self.rollback()
            return False
        else:
            cursor.close()
            return True

    def query(self, operation, parameters=None, fetchone=False):
        conn = self.dbpool.getconn()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        rows = None

        try:
            if parameters:
                cursor.execute(operation, parameters)
            else:
                cursor.execute(operation)

            if fetchone:
                rows = cursor.fetchone()
            else:
                rows = cursor.fetchall()

        except:
            traceback.print_exc()
            cursor.close()
            self.dbpool.putconn(conn, close=True)
            return False
        else:
            cursor.close()
            self.dbpool.putconn(conn)
            return rows

    def query1(self, operation, parameters=None, fetchone=False):
        conn = self.dbpool.getconn()
        rows = []
        try:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            if parameters:
                cursor.execute(operation, parameters)
            else:
                cursor.execute(operation)

            if fetchone:
                rows = cursor.fetchone()
            else:
                rows = cursor.fetchall()

        except:
            traceback.print_exc()
            cursor.close()
            return False
        else:
            cursor.close()
            return rows

    def begin(self):
        self.in_transaction = True
        self.conn = self.dbpool.getconn()

    def commit(self):
        if self.in_transaction and self.conn:
            try:
                self.conn.commit()
            except:
                self.conn.rollback()
                self.dbpool.putconn(self.conn, close=True)
                traceback.print_exc()
            else:
                self.dbpool.putconn(self.conn)
            finally:
                self.in_transaction = False

    def rollback(self):
        if self.in_transaction and self.conn:
            try:
                self.conn.rollback()
            except Exception, ex:
                print ex
                traceback.print_exc()
            finally:
                self.dbpool.putconn(self.conn, close=True)
                self.in_transaction = False


if __name__ == "__main__":
    print MPPG().query("SELECT now() AS time;")
