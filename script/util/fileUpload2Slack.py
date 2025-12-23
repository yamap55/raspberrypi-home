"""
ファイルをSlackに投稿します

メッセージが指定されている場合にはファイル投稿前にメッセージが投稿されます
"""

import argparse
import os
import json
from slack_sdk import WebClient

SETTING_FILE_PATH = '/home/yamap55/raspberrypi-home/config.json'

def main():
    parser = argparse.ArgumentParser(description='ファイルをSlackに投稿するスクリプト')
    parser.add_argument('filePath', help='投稿するファイルPATH')
    parser.add_argument('channel', help='投稿するチャンネルID')
    parser.add_argument('-n', '--fileName', help='投稿する際に表示するファイル名')
    parser.add_argument('-m', '--message', help='ファイル投稿前に投稿するメッセージ')

    args = parser.parse_args()
    filePath = args.filePath
    channel_id = args.channel
    fileName = args.fileName if args.fileName else os.path.basename(filePath)
    message = args.message

    with open(SETTING_FILE_PATH, 'r') as f:
        config  = json.load(f)
        slack = WebClient(token=config['SLACK_TOKEN'])
        if (args.message):
            slack.chat_postMessage(channel=channel_id, text=args.message)

        with open(filePath, 'rb') as file_content:
            slack.files_upload_v2(
                file=file_content,
                filename=fileName,
                channel=channel_id
            )

if __name__=='__main__':
    main()
