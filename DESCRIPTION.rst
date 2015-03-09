Asynchronous SMTP client for Tornado
====================================

This is a thin wrapper around `smtplib.SMTP` and `smtplib.SMTP_SSL` that
provides asynchronous functions (coroutines) for use in Tornado
applications. It provides a single class, `tornado_smtp.client.TornadoSMTP`,
which encapsulates either an `SMTP` or `SMTP_SSL` instance. The API has
intentionally been kept the same in order to make usage obvious.
