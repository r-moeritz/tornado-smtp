tornado-smtp
============

An asynchronous SMTP client for Tornado.

Usage
-----

.. code:: python

import tornado.web
from tornado import gen
from email.message import EmailMessage
from tornado_smtp.client import TorndoSMTP

class MailHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        smtp = TornadoSMTP('<smtp-server-address>')
        yield smtp.starttls()
        yield smtp.login('<username>', '<password>')

        msg = EmailMessage()
        msg['Subject'] = 'Test'
        msg['To']      = '<destination-address>'
        msg['From']    = '<sender-address>'
        msg.set_content('Message body')
        
        smtp = yield self.get_smtp_client()
        smtp.send_message(msg)

        self.render('response.html')

Status
------

Alpha. The code hasn't been tested much but seems to work well enough.

License
-------

::

   Copyright (c) Ralph Möritz 2014.

   Permission is hereby granted, free of charge, to any person obtaining a copy of
   this software and associated documentation files (the "Software"), to deal in
   the Software without restriction, including without limitation the rights to
   use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
   of the Software, and to permit persons to whom the Software is furnished to do
   so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all
   copies or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
   SOFTWARE.

