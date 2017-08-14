#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import oauth2
from flask import Flask
from google.appengine.api import urlfetch


CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

app = Flask(__name__)


def oauth_req(url,
              key,
              secret,
              http_method='GET',
              post_body='',
              http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    response, content = client.request(uri=url,
                                       method=http_method,
                                       body=post_body,
                                       headers=http_headers)
    return content


@app.route('/_b/cron/paseLista')
def pase_de_lista():
    home_timeline = oauth_req(
        url='https://api.twitter.com/1.1/statuses/home_timeline.json',
        key=ACCESS_TOKEN,
        secret=ACCESS_TOKEN_SECRET
    )
    return home_timeline

