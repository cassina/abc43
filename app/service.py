# -*- coding: utf-8 -*-
import time

import oauth2
from google.appengine.ext import deferred

from .config import *


def oauth_req(url,
              key=ACCESS_TOKEN,
              secret=ACCESS_TOKEN_SECRET,
              http_method='GET',
              post_body='',
              http_headers=None):
    """

    :param url:
    :param key:
    :param secret:
    :param http_method:
    :param post_body:
    :param http_headers:
    :return:
    """
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    response, content = client.request(uri=url,
                                       method=http_method,
                                       body=post_body,
                                       headers=http_headers)
    return content


def get_time_line():
    """

    :return:
    """
    return oauth_req(
        url=HOME_TIMELINE_URL,
    )


def post_tweet(msg):
    """

    :param msg:
    :return:
    """
    return oauth_req(
        url=POST_TWEET_URL,
        http_method='POST',
        post_body='status={msg}'.format(
            msg=msg,
        )
    )


def format_list(to_format):
    return ''.join(str(a + '\n') for a in to_format)


def format_msg(hashtags, mentions, status, name, idx):
    """

    :param hashtags:
    :param mentions:
    :return:
    """
    # Agregar menciones hasta tener el producto final
    msg = status.format(idx=idx, name=name) + hashtags

    if len(msg) > 140:
        raise ArithmeticError(
            'Tweet is longer than 140 characters.'
        )

    return msg


def pasar_lista(lista, status, hashtags, mentions):
    for idx, name in enumerate(lista):
        msg = format_msg(hashtags=format_list(hashtags),
                         mentions=format_list(mentions),
                         status=status,
                         name=name,
                         idx=idx + 1)
        deferred.defer(post_tweet, msg=msg)
        time.sleep(1)


