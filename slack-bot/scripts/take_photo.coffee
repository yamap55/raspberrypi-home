# Description
#  「ロボ」に対して「写真を撮って」、「写真とって」と話を書けると写真を撮る
#
# Dependencies:
#  特に無し
#
# Configuration:
#  環境設定を書く
#
# Commands:
#  hubot <message> - <message欄にコメントを入れる>
#
# Notes:
#  メモ書き, その他
#
# Author:
#  yamap55

child_process = require('child_process')

module.exports = (robot) ->
  robot.respond /(写真|しゃしん)を?[撮と]って/, (msg) ->
    msg.send("シャシントリマスヨ")
    child_process.exec "bash /home/yamap55/raspberrypi-home/script/takePhoto.sh", (error, stdout, stderr) ->
