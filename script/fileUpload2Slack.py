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
# filepath, channel, [message]
argvs = sys.argv
if (len(argvs) < 3):
    print "args is required."
    quit()

filePath = argvs[1]
channel = "#" + argvs[2]

if (len(argvs) >= 4):
    message = argvs[3]
    token = os.environ["SLACK_TOKEN"]

    slack = Slacker(token)
    slack.chat.post_message(channel, message)

slack.files.upload(filePath, filename="cap.png",channels=channel)

