# vim: set fileencoding=utf-8 :

from requests_oauthlib import OAuth1
import restmapper
import os

APP_KEY = os.environ['APP_KEY']
APP_SECRET = os.environ['APP_SECRET']
OAUTH_TOKEN = os.environ['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = os.environ['OAUTH_TOKEN_SECRET']

Twitter = restmapper.RestMapper("https://api.twitter.com/1.1/", url_transformer=lambda url: url + ".json")
auth = OAuth1(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter = Twitter(auth=auth)

response = twitter.POST.account.update_profile(description="☁")

