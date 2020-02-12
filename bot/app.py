import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi
from builder import construct_payload

# Initialize a Flask app to host the events adapter
app = Flask(__name__)

# Initialize a Web API client
slack_web_client = WebClient(
    token='')


def start_onboarding(channel: str):
    # Get the onboarding message payload
    message = construct_payload({
        "type": "section",
        "text": {
                "type": "mrkdwn",
                "text": "*Your daily dose of motivation* :blush:"
        }
    },
        {
        "type": "divider"
    },
        {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "The test of the artist does not lie in the will with which he goes to work, but in the excellence of the work he produces... *By <fakeLink.toUser.com|Mark>*"
        }
    })

    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)


start_onboarding('testing')

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000)
