import json
import datetime
import requests
import os


def query(event, context):
    uuid = event['queryStringParameters']['uuid']

    res = requests.get(
            "https://urlscan.io/api/v1/result/{}".format(uuid))

    if res.status_code == 200:
        data = json.loads(res.content)

    response = {
        "statusCode": res.status_code,
        "body": json.dumps(data)
    }

    return response


def submit(event, context):

    post_data = json.loads(event["body"])

    headers = {
        'Content-Type': 'application/json',
        'API-Key': os.environ['api_key']
    }

    res = requests.post(
        'https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(post_data))

    response = {
        "statusCode": 200,
        "body": res.text 
    }

    return response
