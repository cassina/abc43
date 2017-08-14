#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask

from .blueprint import bot

app = Flask(__name__)
app.register_blueprint(bot)




