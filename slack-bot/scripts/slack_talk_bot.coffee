# Description
#  指定されたroomで発言されたメッセージをjsay.shで発声する
#  最後に数字をつけると、それ以前の文字を繰り返す。hoge 2→hoge。hoge。
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
#  ishiguro@moyashi-koubou.com

child_process = require('child_process')

module.exports = (robot) ->
  robot.hear /(.*)$/i, (msg) ->
    text = msg.message.text
    room = msg.envelope.room
    # IDを名前に変換
    room = robot.adapter.client.rtm.dataStore.getChannelGroupOrDMById(room).name
    text_en = encodeURIComponent text

    # 最後が数字かを判別
    if /[0-9]+$|[０-９]+$/.test(text)
        # スペースで分割
        text_split = text.split(/ |　/)
        # 最後を抜き出す
        text_count = text_split.pop()
        # 全角数字だった場合、半角へ変換
        text_count = text_count.replace(/[０-９]/g, (s)->String.fromCharCode(s.charCodeAt(0)-0xFEE0) )
        # テキスト部分を連結
        text = text_split.join("")
        count = 0
        result_text = ""
        while count < text_count
            count++
            result_text = text + "。。" + result_text
        console.log(result_text)
    else
        result_text = text


    # roomの指定
    if (room == "bot_test" || room == "robo_talk")
      # 外部コマンドの実行
      # child_process.exec "sh /usr/local/bin/jsay.sh '#{result_text}'", (error, stdout, stderr) ->

      child_process.exec "sh /home/yamap55/raspberrypi-home/script/util/jsay.sh '#{result_text}'", (error, stdout, stderr) ->
        # コマンド実行した標準出力をbotが話す
        msg.send(stdout)
