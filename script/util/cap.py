import subprocess, sys
import os
import time
from datetime import datetime

basedir = '/home/yamap55/cap/'
cap_resolution = '640x480'

if not os.path.exists(basedir):
    os.makedirs(basedir)

d = datetime.now().strftime("%Y%m%d%H%M%S")
file_path = os.path.join(basedir, f'{d}.jpg', )

cp = subprocess.run(['fswebcam', '-r', cap_resolution, file_path])
if cp.returncode != 0:
    sys.exit(1)

print(file_path)
