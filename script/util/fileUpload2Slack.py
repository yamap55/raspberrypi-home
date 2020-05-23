"""
ファイルをSlackに投稿します

メッセージが指定されている場合にはファイル投稿前にメッセージが投稿されます
"""

import argparse
import os
import json
from slacker import Slacker

SETTING_FILE_PATH = '/home/yamap55/raspberrypi-home/config.json'

def main():
    parser = argparse.ArgumentParser(description='ファイルをSlackに投稿するスクリプト')
    parser.add_argument('filePath', help='投稿するファイルPATH')
    parser.add_argument('channel', help='投稿するチャンネル名')
    parser.add_argument('-n', '--fileName', help='投稿する際に表示するファイル名')
    parser.add_argument('-m', '--message', help='ファイル投稿前に投稿するメッセージ')

    args = parser.parse_args()
    filePath = args.filePath
    channel = args.channel if args.channel[0] == '#' else f'#{args.channel}'
    fileName = args.fileName if args.fileName else os.path.basename(filePath)
    message = args.message

    with open(SETTING_FILE_PATH, 'r') as f:
        config  = json.load(f)
        slack = Slacker(config['SLACK_TOKEN'])
        if (args.message):
            slack.chat.post_message(channel, args.message ,as_user=True)

        slack.files.upload(filePath, filename=fileName, channels=channel)

if __name__=='__main__':
    main()
