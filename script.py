# vim: set fileencoding=utf-8 :

from requests_oauthlib import OAuth1
from restmapper.restmapper import RestMapper
import os
import random

APP_KEY = os.environ['APP_KEY']
APP_SECRET = os.environ['APP_SECRET']
OAUTH_TOKEN = os.environ['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['OAUTH_TOKEN_SECRET']
BIO_FORMAT = os.environ.get('BIO_FORMAT')

Twitter = RestMapper("https://api.twitter.com/1.1/", url_transformer=lambda url: url + ".json")
auth = OAuth1(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter = Twitter(auth=auth)

print BIO_FORMAT

emojis=u"""☁☺☹✊✋☝✌⚡✨⭕❌⭐❕❔❗❓❄☀⛅☔⛄☎➿✂⚽⚾⛳♠♥♣♦☕♤♡♢♧⏰⏳⌛⌚♨✏✒✉⚓⛪⛺⛲⛵✈⛽⚠⛔⬆⬇⬅➡↗↖↘↙◀▶⏪⏩♿㊙㊗✳✴♈♉♊♋♌♍♎♏♐♑♒♓⛎⭕❌©®™⏫⏬↕↔↩↪⤴⤵ℹ❎Ⓜ⚫⚪◼◻▪▫✖➕➖➗➰〰♻☢☣☠☤⚕⚚†☯⚖☮⚘⚔☭⚒⚛⚜☥✠✙✞✟✧⋆★☆✪✫✬✭✮✯✰✡☫☬☸✵❂⚘❀❃❁✼♫♪☃❅❆☂❦♕♛♔♖♜☾→⇒⟹⇨⇰➩➪➫➬➭➮➯➲➳➵➸➻➺➼➽☜☟➹➷↶↷✆⌘⎋⏎⏏⎈⎌⍟❥ツღ☻"""

random_emoji = unicode(random.choice(emojis))
if BIO_FORMAT is None:
    description = u"{}".format(random_emoji)
else:
    description = u"{} {}".format(BIO_FORMAT, random_emoji.decode("utf8"))

response = twitter.POST.account.update_profile(description=description, parse_response=False)

