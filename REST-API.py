from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
from tornado.web import url
import mysql.connector
import json

mydb = mysql.connector.connect(
    host="192.168.0.201",
    user="root",
    password="root",
    database="REST-API"
)
mycursor = mydb.cursor()


class GetUsers(tornado.web.RequestHandler):
    def get(self):
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()
        table = []
        for row in myresult:
            my_dict = {"id": row[0], "name": row[1],
                       "email": row[2], "info": "Select all users"}
            table.append(my_dict)
        result = json.dumps(table)
        self.write(result)


class GetUser(tornado.web.RequestHandler):
    def get(self, id):
        # In build
        sql = "INSERT INTO users (name, email) VALUES (%s)"
        val = (id)
        mycursor.execute(sql, val)
        result = {"info": "Insert new user"}
        self.write(json.dumps(result))


class AddUser(tornado.web.RequestHandler):
    def post(self, name, email):
        self.set_header("Content-Type", "text/plain")
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        val = (name, email)
        mycursor.execute(sql, val)
        result = {"info": "Insert new user"}
        self.write(json.dumps(result))


class PutUser(tornado.web.RequestHandler):
    def put(self, name, email, id):
        sql = ("UPDATE users SET name=", name,
               ", email=", email, " WHERE id=", id)
        mycursor.execute(sql)
        result = {"info": "Edit new user"}
        self.write(json.dumps(result))


application = tornado.web.Application([
    (r"/users/([0-9]+)/(.*)/(.*)", PutUser),  # Edit user [id/name/email]
    (r"/users",  GetUsers),  # Get users
    (r'/users/([0-9]+)', GetUser),  # Get user by id - currently in build
    (r"/users/(.*)/(.*)", AddUser)  # Insert new user [name/email]

])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
