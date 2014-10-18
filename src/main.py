import tornado.ioloop
import tornado.web
import tornado.log
from tornado.web import RequestHandler

from db import connect

tornado.log.enable_pretty_logging()
# import logging
# logging.basicConfig(level=logging.DEBUG)


class MainHandler(RequestHandler):
    def get(self):
        self.render('home.html')


class LoginHandler(BaseRequestHandler):
    def get(self):
        if self.current_user is not None:
            return self.redirect('/')

        self.render('login.html', messages=None)

    def post(self):
        username = self.get_argument('username')
        hashed_password = hash_password(self.get_argument('password'))

        user = self.db.get_user(username)
        if user is None:
            error = 'No such user as "{}"'.format(username)
            logger.info(error)
            return self.render('login.html', messages=[error])

        if user.hashed_password != hashed_password:
            error = 'Incorrect password for "{}"'.format(username)
            logger.info(error)
            return self.render('login.html', messages=[error])

        assert user.uid is not None
        self.set_secure_cookie('uid', user.uid)

        return self.redirect('/')


class LogoutHandler(BaseRequestHandler):
    def get(self):
        self.set_secure_cookie('uid', '')


settings = {
    'debug': True,
    'template_path': 'templates',
    'cookie_secret': 'perthstudenthack'
}


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login", LoginHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)

    application.db = connect()

    tornado.ioloop.IOLoop.instance().start()

    application.db.shutdown()
