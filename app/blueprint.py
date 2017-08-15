# -*- coding: utf-8 -*-
from flask import Blueprint

from .service import format_msg, post_tweet, format_list, pasar_lista, get_time_line
from .lists import *

bot = Blueprint('bot', __name__)


@bot.route('/_b/cron/smoke', methods=['GET'])
def pasar_lista_43():
    return 'ok'


@bot.route('/_b/cron/pasarLista43', methods=['GET'])
def pasar_lista_43():
    pasar_lista(lista=normalistas,
                status=status_43,
                hashtags=hashtags_43,
                mentions=responsables)

    return '#FueElEstado #PaseDeLista1al43 . DONE'


@bot.route('/_b/cron/pasarListaABC', methods=['GET'])
def pasar_lista_abc():
    pasar_lista(lista=abc,
                status=status_abc,
                hashtags=hashtags_abc,
                mentions=responsables)


@bot.route('/_b/tweets/delete', methods=['GET'])
def delete_tweets():
    timeline = get_time_line()
    return timeline