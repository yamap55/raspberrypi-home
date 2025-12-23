#!/bin/bash
# 写真撮ってSlackにあげるScript
source /home/yamap55/raspberrypi-home/.venv/bin/activate
basedir=/home/yamap55/raspberrypi-home/script/
${basedir}util/jsay.sh "ロボです。写真撮りますよ。3。2。1。"
filePath=`python3 ${basedir}util/cap.py`
if [ $? -gt 0 ]; then
    ${basedir}util/jsay.sh "ロボです。写真が撮れませんでした。パパに連絡してください。"
    exit 1
fi
${basedir}util/jsay.sh "ロボです。写真撮りました。"
python3 ${basedir}util/fileUpload2Slack.py ${filePath} C8Q8UQ71D -m ロボガシャシントリマシタ。
# node /home/yamap55/raspberrypi-home/googledrive/googledrive-upload.js ${filePath}
