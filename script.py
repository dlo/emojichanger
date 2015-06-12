# vim: set fileencoding=utf-8 :

from requests_oauthlib import OAuth1
from restmapper.restmapper import RestMapper
import os
import random

APP_KEY = os.environ['APP_KEY']
APP_SECRET = os.environ['APP_SECRET']
OAUTH_TOKEN = os.environ['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['OAUTH_TOKEN_SECRET']

Twitter = RestMapper("https://api.twitter.com/1.1/", url_transformer=lambda url: url + ".json")
auth = OAuth1(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter = Twitter(auth=auth)

emojis=u"""☁☺☹✊✋☝✌⚡✨⭕❌⭐❕❔❗❓❄☀⛅☔⛄☎➿✂⚽⚾⛳♠♥♣♦☕♤♡♢♧⏰⏳⌛⌚♨✏✒✉⚓⛪⛺⛲⛵✈⛽⚠⛔⬆⬇⬅➡↗↖↘↙◀▶⏪⏩♿㊙㊗✳✴♈♉♊♋♌♍♎♏♐♑♒♓⛎⭕❌©®™⏫⏬↕↔↩↪⤴⤵ℹ❎Ⓜ⚫⚪◼◻▪▫✖➕➖➗➰〰♻☢☣☠☤⚕⚚†☯⚖☮⚘⚔☭⚒⚛⚜☥✠✙✞✟✧⋆★☆✪✫✬✭✮✯✰✡☫☬☸✵❂⚘❀❃❁✼♫♪☃❅❆☂❦♕♛♔♖♜☾→⇒⟹⇨⇰➩➪➫➬➭➮➯➲➳➵➸➻➺➼➽☜☟➹➷↶↷✆⌘⎋⏎⏏⎈⎌⍟❥ツღ☻"""

response = twitter.POST.account.update_profile(description=u"Pressing buttons and breaking things. Follow @dwlz_ for higher tweet bandwidth. EOTD: {}.".format(random.choice(emojis)), parse_response=False)

