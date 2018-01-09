#!/bin/bash

# 写真撮ってSlackにあげるScript

basedir=/home/yamap55/raspberrypi-home/script/
${basedir}util/jsay "ロボです。写真撮りますよ。3。2。1。"
filePath=`${basedir}util/cap.py`
${basedir}util/jsay "ロボです。写真撮りました。"
${basedir}util/fileUpload2Slack.py ${filePath} photo ロボガシャシントリマシタ。

