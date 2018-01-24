#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twitter import *
import sys
import os

# TwitterでTweetします。
#
# 引数
# message
#
# 環境変数
# TWITTER_TOKEN
# TWITTER_TOKEN_SECRET
# TWITTER_COSUMER_KEY
# TWITTER_COSUMER_SECRET
#
# 参考
# https://apps.twitter.com/
# https://github.com/sixohsix/twitter

token = os.environ["TWITTER_TOKEN"]
token_secret = os.environ["TWITTER_TOKEN_SECRET"]
consumer_key = os.environ["TWITTER_COSUMER_KEY"]
consumer_secret = os.environ["TWITTER_COSUMER_SECRET"]

t = Twitter(
            auth=OAuth(token, token_secret, consumer_key, consumer_secret))
#t.statuses.update(status="Using @sixohsix's sweet Python Twitter Tools.")
aaa=t.statuses.update(status=sys.argv[1])
print aaa

