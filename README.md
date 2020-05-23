# Raspberry Pi @ home
我が家のRaspberry Piで動いている奴等です。

## 環境作成
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get install open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001

git clone https://github.com/yamap55/raspberrypi-home.git
cd raspberrypi-home

python3 -m venv .venv
pip install --upgrade pip
pip install -r requirements.txt

# TOKEN設定
cp ./config_template.json ./config.json
vi ./config.json

# TODO: 
mkdir secret
vi ./secret/birthday-list.txt

crontab ./crontab.bk
```

## script
- crontab.bk
  - cronのバックアップ。
- takePhoto.sh
  - 写真を撮ってSlackに投げ込むSript。
- time_report.sh
  - 時報をお知らせするScript。

### util
- cap.py
  - Raspberry Piに接続されているカメラで写真を撮る。
- fileUpload2Slack.py
  - ファイルをSlackにアップロード。
- jsay.sh
  - 指定された文章を喋る。

## slack-bot
- hubot

## 参考にさせて頂いたblogとか
- [割と本気で家庭用Slack Botを作ってみた](http://blog.8arrow.org/entry/2016/01/13/183349)
- [子どもがいる家庭で使うRaspberryPi＆Slack](https://www.moyashi-koubou.com/blog/raspi_slack_for_children/)

