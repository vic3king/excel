from apscheduler.schedulers.background import BackgroundScheduler

# jobs
from bot.post_message import post_quote_to_channel

scheduler = BackgroundScheduler()

scheduler.add_job(
    post_quote_to_channel,
    'interval',
    seconds=10
)
