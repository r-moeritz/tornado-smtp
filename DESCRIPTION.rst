Asynchronous SMTP client for Tornado
====================================

This is an thin wrapper around `smtplib.SMTP` and `smtplib.SMTP_SSL` that
provides asynchronous functions (coroutines) for use in Tornado
applications. It provides a single class, `tornado_smtp.client.TornadoSMTP`,
which encapsulates either an `SMTP` or `SMTP_SSL` instance. The API has been
intentionally kept the same in order to make usage obvious.
