from slacker import Slacker
import datetime
import os
import json

SETTING_FILE_PATH = '/home/yamap55/raspberrypi-home/config.json'
NOTIFICATION_CHANNEL = '#random'

today = datetime.date.today()
tyear = today.year
tday = today.day
tmonth = today.month

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

            with open(SETTING_FILE_PATH, 'r') as f:
                config  = json.load(f)
                slack = Slacker(config['SLACK_TOKEN'])
                slack.chat.post_message(NOTIFICATION_CHANNEL, message.format(y), as_user=True)
