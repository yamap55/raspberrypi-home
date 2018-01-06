#!/bin/bash

m=`date +%M`

time="`date +%l`時"
if [ "${m}" != "00" ] ; then
  time="${time}${m}分"
fi

message="ロボです。${time}をお知らせします。"
result=`/home/yamap55/raspberrypi-home/script/jsay "$message"`

echo `date "+%Y/%m/%d %H:%M:%S"` ${result} >> /home/yamap55/raspberrypi-home/script/logs/time_report.log

