__author__ = 'kaushik'
import mysql.connector


class DB:
    def init(self):
        self.conn = mysql.connector.connect \
            (user='root', password='', host='127.0.0.1', database=self.db)
        self.cursor = self.conn.cursor()

    def __init__(self, db='mining'):
        self.db = db
        self.init()

    def get_data(self, sql):
        try:
            self.init()
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
        finally:
            self.done()
        return rows

    def done(self):
        self.conn.close()


class Subdue:
    def __init__(self):
        self.db = DB('caida')

    def maadi(self):
        ips = self.db.get_data("select id from ips order by id")
        for i in ips:
            # print "v %d foo_%d" % (i[0], i[0] % 100)
            print "v %d vlabel_%d" % (i[0], 100)
        data = self.db.get_data("select s_ip, d_ip from der")
        for d in data:
            print "e %d %d elabel_%d" % (d[0], d[1], 100)


# Subdue().maadi()
