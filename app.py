import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi
from bot.jobs import scheduler
from bot.post_message import post_quote_to_channel
# Initialize a Flask app to host the events adapter
app = Flask(__name__)

# Initialize a Web API client
post_quote_to_channel()
# @manager.command
# def start_scheduler():
#     scheduler.start()

if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(port=3000)
