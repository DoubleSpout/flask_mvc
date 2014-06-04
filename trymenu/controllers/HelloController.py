# -*- coding: utf-8 -*-
from trymenu import app
from flask import render_template, request
from trymenu.models import HelloModel
from trymenu.bussiness import LoggerBl

@app.route('/')
def index():
    return "Flask MVC!"


@app.route('/hello/<uname>')
def hello(uname=None):
    hello = HelloModel.Hello(uname)
    text = hello.MyName()
    LoggerBl.logger.info('start')
    return render_template('hello.html',name=text)

