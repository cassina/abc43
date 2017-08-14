# -*- coding: utf-8 -*-
from flask import Blueprint

from .service import format_msg, post_tweet, format_list, pasar_lista
from .lists import *

bot = Blueprint('bot', __name__)


@bot.route('/_b/cron/pasarLista43', methods=['GET'])
def pasar_lista_43():
    # for idx, name in enumerate(normalistas):
        # count = idx
        # if idx == 5:
        #     return 'DONE'
        # msg = format_msg(hashtags=format_list(hashtags_43),
        #                  mentions=format_list(responsables),
        #                  status=status_43,
        #                  name=name,
        #                  idx=idx)
        # post_tweet(msg)
    pasar_lista(lista=normalistas,
                status=status_43,
                hashtags=hashtags_43,
                mentions=responsables)

    return '#FueElEstado #PaseDeLista1al43 . DONE'


@bot.route('/_b/cron/pasarListaABC', methods=['GET'])
def pasar_lista_abc():
    # for idx, name in enumerate(normalistas):
    # count = idx
    # if idx == 5:
    #     return 'DONE'
    # msg = format_msg(hashtags=format_list(hashtags_43),
    #                  mentions=format_list(responsables),
    #                  status=status_43,
    #                  name=name,
    #                  idx=idx)
    # post_tweet(msg)
    pasar_lista(lista=abc,
                status=status_abc,
                hashtags=hashtags_abc,
                mentions=responsables)
