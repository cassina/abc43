#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import tweetpony
from flask import Flask

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

app = Flask(__name__)
tw = tweetpony.API(
    CONSUMER_KEY,
    CONSUMER_KEY,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)


@app.route('/_b/cron/paseLista')
def pase_de_lista():
    try:
        tw.update_status(status='This is a tweet!')
        return 'Hello'
    except tweetpony.APIError as e:
        print(e.code)
        print(e.description)
