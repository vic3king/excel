from apscheduler.schedulers.background import BlockingScheduler

# jobs
from bot.post_message import post_quote_to_channel

scheduler = BlockingScheduler()

scheduler.add_job(
    post_quote_to_channel,
    'cron',
    hour=18
)
