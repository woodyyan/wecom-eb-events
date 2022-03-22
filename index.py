# -*- coding: utf8 -*-
import json

import requests

template = '''
    {
    "msgtype": "markdown",
    "markdown": {
        "content": "%s"
    }
}
'''


def main_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("Received context: " + str(context))

    event_list = event['EventList']
    contents = ''
    for single_event in event_list:
        content = single_event['data']['markdown']['content']
        contents += content + '\n\n'

    print(contents)

    data = template % contents

    r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=81ef7bfa-0ff4-4850-86df-a8e272c8cafe',
                      data=data.encode('utf-8'))
    print(r.status_code)
    print(r.content)
