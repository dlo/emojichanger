emojichanger
============

Setting up deployments
----------------------

```
heroku git:remote -a twitter-profile-updater
```

```
heroku create
git push heroku master
heroku config:set APP_KEY="YOUR_APP_KEY"
heroku config:set APP_SECRET="YOUR_APP_SECRET"
heroku config:set OAUTH_TOKEN="YOUR_OAUTH_TOKEN"
heroku config:set OAUTH_TOKEN_SECRET="YOUR_OAUTH_TOKEN_SECRET"
heroku addons:create scheduler:standard
```

Optionally, you can also provide a bio to prepend the random Emoji.

```
heroku config:set BIO_FORMAT="Linguist. Philosopher. Millenial."
```

Set up a recurring task for every X minutes that calls `python script.py`.

...and you're done!
