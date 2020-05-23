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

# キリ番？か確認する
# https://blanktar.jp/blog/2015/06/python-check-kiriban.html
def isKiri(x):
    if re.match('^([0-9])\\1{3,}$', str(x)):  # ゾロ目（4桁以上）
        return True
    if re.match('^[0-9]000+$', str(x)):  # 100とか200とか。（1000以上）
        return True
    if x > 999 and str(x) in '01234567890' or str(x) in '09876543210':  # 連番（1000以上）
        return True
    return False

with open("/home/yamap55/raspberrypi-home/secret/birthday-list.txt", "r") as f:
    for line in f.readlines():
        # 1987/05/14,今日はhogeの誕生日:{0}歳
        # 1987/05/14,hoge,birthday
        ar = line.replace("\n", "").split(",")
        if len(ar) < 3:
            continue
        date = ar[0]
        name = ar[1]
        datetype = ar[2]

        message = ""
        if datetype == "birtyday" :
            tdatetime = datetime.datetime.strptime(birthday, "%Y/%m/%d")
            if tdatetime.day == tday and tdatetime.month == tmonth :
                # 誕生日
                y = tyear - tdatetime.year
                message = ":birthday:今日は{0}の誕生日:tada: : {1}歳".format(name, y)
                slack.chat.post_message(channel, message, username="誕生日", icon_emoji=":birthday:")
            elif isKiri((today - tdatetime).day % 1000) :
                # 生誕何日のキリ番
                message = "{0}が産まれてから{1}日経過しました！"
                slack.chat.post_message(channel, message, username="誕生日キリ番", icon_emoji=":birthday:")
