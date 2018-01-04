#!/bin/bash

# HTSVOICE=/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice
HTSVOICE=/usr/share/hts-voice/mei/mei_normal.htsvoice

voice=`tempfile`
option="-m $HTSVOICE \
  -s 16000 \
  -p 100 \
  -a 0.03 \
  -u 0.0 \
  -jm 1.0 \
  -jf 1.0 \
  -x /var/lib/mecab/dic/open-jtalk/naist-jdic \
  -ow $voice"

if [ -z "$1" ] ; then
  open_jtalk $option
else
  if [ -f "$1" ] ; then
    open_jtalk $option $1
  else
    echo "$1" | open_jtalk $option
  fi
fi

aplay -q $voice
rm $voice

echo -n "オハナシシタヨ : 「$1」"

