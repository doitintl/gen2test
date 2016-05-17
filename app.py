import MySQLdb
import os
import webapp2


class IndexPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            db = MySQLdb.connect(unix_socket='/cloudsql/gen2test-1285:us-central1:gen2test', user='root',
                                 passwd='g00gleit!')
        else:
            db = MySQLdb.connect(host='localhost', user='root')

        cursor = db.cursor()
        cursor.execute('SHOW VARIABLES')
        for r in cursor.fetchall():
            self.response.write('%s\n' % str(r))

        db.commit()
        db.close()


class Page1(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            db = MySQLdb.connect(unix_socket='/cloudsql/gen2test-1285:us-central1:gen2test', user='root',
                                 passwd='g00gleit!')
        else:
            db = MySQLdb.connect(host='localhost', user='root')

        cursor = db.cursor()
        cursor.execute('CREATE DATABASE gen2test;')
        db.commit()
        db.close()


class Page2(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            db = MySQLdb.connect(unix_socket='/cloudsql/gen2test-1285:us-central1:gen2test', user='root',
                                 passwd='g00gleit!', db='gen2test')
        else:
            db = MySQLdb.connect(host='localhost', user='root')

        cursor = db.cursor()
        cursor.execute('CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);')
        db.commit()
        db.close()


class Page3(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            db = MySQLdb.connect(unix_socket='/cloudsql/gen2test-1285:us-central1:gen2test', user='root',
                                 passwd='g00gleit!', db='gen2test')
        else:
            db = MySQLdb.connect(host='localhost', user='root')

        cursor = db.cursor()
        cursor.execute('INSERT INTO pet (name,owner,species,sex,birth,death) VALUES (\'Jet\',\'Ramesh\',\'dog\', \'f\', CURDATE(), CURDATE());')
        db.commit()

        db.close()


class Page4(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'

        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            db = MySQLdb.connect(unix_socket='/cloudsql/gen2test-1285:us-central1:gen2test', user='root',
                                 passwd='g00gleit!', db='gen2test')
        else:
            db = MySQLdb.connect(host='localhost', user='root')

        cursor = db.cursor()
        cursor.execute('select * from pet')
        t = cursor.fetchall()
        self.response.write(len(t))
        for r in t:
            self.response.write('%s\n' % str(r))

        db.commit()
        db.close()


app = webapp2.WSGIApplication([
    ('/', IndexPage),
    ('/1', Page1),
    ('/2', Page2),
    ('/3', Page3),
    ('/4', Page4)
])
