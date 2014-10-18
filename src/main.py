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

        self.render('login.html')

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        password = pbkdf2_sha256.

        if not self.user_exists(username):
            return

        import IPython
        IPython.embed()

        self.set_secure_cookie('uid', value)


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
