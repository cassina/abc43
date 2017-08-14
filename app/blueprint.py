# -*- coding: utf-8 -*-
from flask import Blueprint

from .service import format_msg, post_tweet, format_list
from .lists import *

bot = Blueprint('bot', __name__)


@bot.route('/_b/cron/pasarLista43', methods=['GET'])
def pasar_lista():
    msg = format_msg(hashtags=format_list(hashtags_43),
                     mentions=format_list(responsables),
                     status=status_43)
    return post_tweet(msg)
