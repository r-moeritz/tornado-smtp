import os
import functools
from socket import _GLOBAL_DEFAULT_TIMEOUT
from smtplib import SMTP, SMTP_SSL
from concurrent.futures import ThreadPoolExecutor
from tornado import gen

class TornadoSMTP:
    def initialized_async(func):
        @functools.wraps(func)
        @gen.coroutine
        def wrapper(self, *args, **kwargs):
            if self._busy:
                self._smtp = yield self._busy
                self._busy = None
            
            result = yield func(self, *args, **kwargs)
            return result
    
        return wrapper

    def __init__(self, host='', port=0, local_hostname=None, timeout=_GLOBAL_DEFAULT_TIMEOUT, 
                 source_address=None, use_ssl=False, keyfile=None, certfile=None, context=None):
        self._pool = ThreadPoolExecutor(os.cpu_count() or 1)
        self._busy = self._pool.submit(self._initialize, host, port, local_hostname, timeout,
                                       source_address, use_ssl, keyfile, certfile, context)
    
    def _initialize(self, host='', port=0, local_hostname=None, timeout=_GLOBAL_DEFAULT_TIMEOUT, 
                    source_address=None, use_ssl=False, keyfile=None, certfile=None, context=None):
        return (SMTP_SSL(host, port, local_hostname, keyfile, certfile, timeout, context, source_address)
                if use_ssl else SMTP(host, port, local_hostname, timeout, source_address))

    @initialized_async
    def login(self, user, password):
        return self._pool.submit(self._smtp.login, user, password)

    @initialized_async
    def starttls(self, keyfile=None, certfile=None, context=None):
        return self._pool.submit(self._smtp.starttls, keyfile, certfile, context)

    @initialized_async
    def send_message(self, msg, from_addr=None, to_addrs=None, mail_options=(), rcpt_options=()):
        return self._pool.submit(self._smtp.send_message, msg, from_addr, to_addrs, mail_options, rcpt_options)

    @initialized_async
    def quit(self):
        return self._pool.submit(self._smtp.quit)