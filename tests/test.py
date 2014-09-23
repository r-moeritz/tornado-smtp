#! python

import tornado.web
from email.message import EmailMessage
from tornado import gen
from tornado.options import options
from tornado.ioloop import IOLoop
from tornado_smtp.client import TornadoSMTP

FROM_ADDR     = '<your@email.address>'
SMTP_SERVER   = '<your-smtp.server>'
SMTP_USER     = '<your_user_name>'
SMTP_PASSWORD = '<your_password>'

options.define('port', default=8888, help='run on the given port', type=int)

class TestApplication(tornado.web.Application):
    @gen.coroutine
    def get_smtp_client(self):
        smtp = TornadoSMTP(SMTP_SERVER)
        yield smtp.starttls()
        yield smtp.login(SMTP_USER, SMTP_PASSWORD)
        return smtp

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    @gen.coroutine
    def post(self):
        msg = EmailMessage()
        msg['Subject'] = self.get_argument('subject')
        msg['To']      = self.get_argument('email')
        msg['From']    = FROM_ADDR
        msg.set_content(self.get_argument('message'))
        
        smtp = yield self.application.get_smtp_client()
        smtp.send_message(msg)

        self.render('index.html')

def main():
    options.parse_command_line()
    app = TestApplication([ (r'/', MainHandler) ])
    app.listen(options.port)
    IOLoop.instance().start()

main()