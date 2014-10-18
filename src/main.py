import tornado.ioloop
import tornado.web
import tornado.log
from tornado.web import RequestHandler


tornado.log.enable_pretty_logging()
# import logging
# logging.basicConfig(level=logging.DEBUG)


class MainHandler(RequestHandler):
    def get(self):
        self.render('home.html')

settings = {
    'debug': True,
    'template_path': 'templates'
}


application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
