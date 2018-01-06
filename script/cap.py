#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import os
import os.path
import time
from datetime import datetime

basedir = "/tmp/cap/"
if not os.path.exists(basedir):
    os.mkdir(basedir)
token=os.environ["SLACK_TOKEN"]

def capture():
    d = datetime.now().strftime("%Y%m%d%H%M%S")
    capName = basedir + "cap_" + d + ".jpg"
    c = cv2.VideoCapture(0)
    r, img = c.read()
    cv2.imwrite(capName, img)
    c.release()
    return capName

filePath = capture()
size = os.path.getsize(filePath)
while size == 0:
    # エラーで0byteになる事があるため撮れるまで回す
    os.remove(filePath)
    time.sleep(0.5)
    filePath = capture()
    size = os.path.getsize(filePath)

print filePath
