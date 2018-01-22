#!/usr/bin/env python
# coding: utf-8
from slacker import Slacker
import datetime
from datetime import timedelta
import os

today = datetime.date.today()
tyear = today.year
tday = today.day
tmonth = today.month

token = os.environ["SLACK_TOKEN"]
slack = Slacker(token)
channel = "#random"
#channel = "#test"

with open("/home/yamap55/raspberrypi-home/secret/birthday-list.txt", "r") as f:
    for line in f.readlines():
        # 1987/05/14,今日はhogeの誕生日:{0}歳
        ar = line.replace("\n", "").split(",")
        if len(ar) < 2:
            continue
        birthday = ar[0]
        message = ar[1]
        tdatetime = datetime.datetime.strptime(birthday, "%Y/%m/%d")

        if tdatetime.day == tday and tdatetime.month == tmonth:
            y = tyear - tdatetime.year
            slack.chat.post_message(channel, message.format(y),as_user=True)
