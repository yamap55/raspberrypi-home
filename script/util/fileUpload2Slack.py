#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ファイルをSlackに投げます。
# メッセージが指定されている場合にはメッセージを投げてからファイルを投げます。
#
# 引数
# filepath, channel, [message]
#
# 環境変数「SLACK_TOKEN」が必須

from slacker import Slacker
import sys
import os

# 引数
# filepath, channel, fileName, [message]
argvs = sys.argv
if (len(argvs) < 4):
    print "args is required."
    quit()

filePath = argvs[1]
channel = "#" + argvs[2]
fileName = argvs[3]

token = os.environ["SLACK_TOKEN"]
slack = Slacker(token)
if (len(argvs) >= 5):
    message = argvs[4]
    slack.chat.post_message(channel, message)

slack.files.upload(filePath, filename=fileName, channels=channel)

