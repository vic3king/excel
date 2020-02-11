import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi
from builder import OnboardingTutorial



# {"channel": {"user_id": OnboardingTutorial}}
# onboarding_tutorials_sent = {}

def start_onboarding(channel: str):
    # Create a new onboarding tutorial.
    onboarding_tutorial = OnboardingTutorial(channel)

    # Get the onboarding message payload
    message = onboarding_tutorial.get_message_payload()

    print(message)
    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)



start_onboarding('random')

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000)
