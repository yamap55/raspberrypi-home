# Description
#  #gym_record で指定フォーマットで発言されたメッセージをスプレッドシートに記録する
#
# Dependencies:
#  特に無し
#
# Configuration:
#  HUBOT_GYM_RECODE_SPREADSHEET_ID
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
GoogleSpreadsheet = require('google-spreadsheet');
module.exports = (robot) ->
  robot.hear /日付 : (.*)\s時間 : (.*)\s距離 : (.*)\s備考 : (.*)/i, (msg) ->
    gymDate = msg.match[1];
    gymTime = msg.match[2];
    gymRange = msg.match[3];
    gymMemo = msg.match[4];

    room = msg.envelope.room
    # IDを名前に変換
    room = robot.adapter.client.rtm.dataStore.getChannelGroupOrDMById(room).name
    if (room != "gym_record" && room != "test")
      return

    spreadsheet = new GoogleSpreadsheet(process.env.HUBOT_GYM_RECODE_SPREADSHEET_ID)
    credentials = require("/home/yamap55/raspberrypi-home/secret/home-project-897719f1369e.json");

    interval = 0
    gymCount = 0
    spreadsheet.useServiceAccountAuth(credentials, (err) ->
      spreadsheet.getInfo((err, sheets) ->
        sheet = (i for i in sheets.worksheets when i.title == "記録")[0]
        gymCount = sheet.rowCount

        # Twitterに投げるために前回の記録から日付を取得
        sheet.getRows({"offset": sheet.rowCount - 1}, (err, rows) ->
          if (err == null)
            interval = (new Date("2018-01-29").getTime() - new Date(gymDate).getTime())/(1000*60*60*24)
          else
            msg.send("Tweetジュンビニシッパイシマシタ : " + err)
            return
        )

        # Spreadsheetに書込み
        sheet.addRow({"日付" : gymDate,"時間" : gymTime,"距離" : gymRange,"備考" : gymMemo},
          (err, row) ->
            if (err == null)
              msg.send("Spreadsheetニカキコミマシタ")
            else
              msg.send("Spreadsheetノカキコミニシッパイシマシタ : " + err)
        );
      );
    );
    # Twitterに投げる
    message = "#ジム #プール 完了。#{interval}日ぶり#{gymCount}回目、#{gymTime}hで#{gymRange}m。#{gymMemo}"
    if (message.length > 140)
      msg.send("140モジイジョウナノデツイートシナイヨ : " + message.length + "モジ\n" + message)
    else
      child_process.exec "/home/yamap55/raspberrypi-home/script/util/tweet.py '#{message}'", (error, stdout, stderr) ->
        if !error
          msg.send("ツイートシタヨ : " + stdout)
        else
          msg.send("ツイートニシッパイシタヨ : " + stderr)
