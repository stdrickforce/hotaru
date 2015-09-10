#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created At: Thu Sep 10 22:16:05 2015
# Updated At: Thu Sep 10 22:16:05 2015

__author__ = "stdrickforce"  # Tengyuan Fan
# Email: <stdrickforce@gmail.com> <tfan@xingin.com>

from flask import (
    Flask,
    render_template,
)

from inori.settings import (
    DEBUG,
    SECRET_KEY,
)

from inori.views import api


def not_found(error):
    return render_template('404.html'), 404


def init_module(app):
    api.init_app(app)


def init_others(app):
    app.error_handler_spec[None][404] = not_found


def init_config(app):
    app.debug = DEBUG
    app.secret_key = SECRET_KEY


def create_app():
    app = Flask(__name__)
    init_config(app)
    init_others(app)
    init_module(app)
    return app

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1720)
