#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from datetime import datetime

import oauth2
from flask import Flask

from .lists import *

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

HOME_TIMELINE_URL = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
POST_TWEET_URL = 'https://api.twitter.com/1.1/statuses/update.json'

app = Flask(__name__)


def oauth_req(url,
              key=ACCESS_TOKEN,
              secret=ACCESS_TOKEN_SECRET,
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


def get_time_line():
    return oauth_req(
        url=HOME_TIMELINE_URL,
    )


def post_tweet(msg):
    return oauth_req(
        url=POST_TWEET_URL,
        http_method='POST',
        post_body='status={msg}&lat={lat}&long={lo}'.format(
            msg=msg,
            lat=lat,
            lo=lo
        )
    )


def format_list(to_format):
    return ''.join(str(a + '\n') for a in to_format)


def format_msg():
    mentions = format_list(responsables)
    hashes = format_list(hashtags)
    msg = status_43.format(idx='1', name='Yo') + hashes #+ mentions agregar menciones hasta tener el producto final
    if len(msg) > 140:
        print('LONGER LONGER')
        raise ArithmeticError(
            'Tweet is longer than 140 characters.'
        )
    return msg


@app.route('/_b/cron/pasarLista', methods=['GET'])
def pasar_lista():
    msg = format_msg()
    print(msg)
    resp = post_tweet(msg)
    return resp



