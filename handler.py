import json
import os


def hello(event, context):
    body = {
        "Service": os.environ["service"],
        "Username": os.environ["username"],
        "Password": os.environ["password"],
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
