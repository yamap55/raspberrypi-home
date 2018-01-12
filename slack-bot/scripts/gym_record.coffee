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

GoogleSpreadsheet = require('google-spreadsheet');
module.exports = (robot) ->
  robot.hear /日付 : (.*)\s時間 : (.*)\s距離 : (.*)\s備考 : (.*)/i, (msg) ->
    room = msg.envelope.room
    # IDを名前に変換
    room = robot.adapter.client.rtm.dataStore.getChannelGroupOrDMById(room).name
    if (room != "gym_record" && room != "test")
      return

    spreadsheet = new GoogleSpreadsheet(process.env.HUBOT_GYM_RECODE_SPREADSHEET_ID)
    credentials = require("/home/yamap55/raspberrypi-home/secret/home-project-897719f1369e.json");

    spreadsheet.useServiceAccountAuth(credentials, (err) ->
      spreadsheet.getInfo((err, sheets) ->
        sheet = (i for i in sheets.worksheets when i.title == "記録")[0]
        sheet.addRow({"日付" : msg.match[1],"時間" : msg.match[2],"距離" : msg.match[3],"備考" : msg.match[4]},
                     (err, row) ->
                       if (err == null)
                         msg.send("Spreadsheetニカキコミマシタ")
                       else
                         msg.send("Spreadsheetノカキコミニシッパイシマシタ : " + err)
                     );
      );
    );
