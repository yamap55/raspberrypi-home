cron = require('cron').CronJob
# test script
module.exports = (robot) ->
  new cron '0 0 1 1 * *', () =>
    robot.send {room: "#test"}, "testメッセージだお"
  , null, true, "Asia/Tokyo"

