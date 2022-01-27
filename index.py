# -*- coding: utf8 -*-
import json
import requests


def main_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("Received context: " + str(context))
