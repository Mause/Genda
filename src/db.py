import sqlite3

from passlib.hash import pbkdf2_sha256


def hash_password(password):
    return pbkdf2_sha256.encrypt(
        password,
        rounds=20000,
        salt_size=16
    )


class User():
    @classmethod
    def from_query(cls, query):
        return User(query[0], query[1])


class Db():
    def __init__(self, connection):
        self.connection = connection

    def get_user(self, uid):
        cursor = self.connection.cursor()

        print(cursor.execute(
            'SELECT * FROM users WHERE uid=?',
            uid
        ))

        return User.from_query(cursor.fetchone())

    def user_exists(self, username):
        cursor = self.connection.cursor()
        query = cursor.execute(
            'SELECT COUNT(*) FROM users WHERE username=?',
            username
        )

        return query.fetchone() != 0

    def create_user(self, username, password):
        password = hash_password(password)

        cursor = self.connection.cursor()

        cursor.execute(
            'INSERT INTO users (username,password) VALUES (?,?)',
            username,
            password
        )

        return User.from_query((username, password))

    def shutdown(self):
        self.connection.close()


def connect():
    return Db(sqlite3.connect('db.db'))
