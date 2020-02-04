from apscheduler.schedulers.background import BackgroundScheduler
from .reminderapi import check_for_reminders


def start():

    scheduler = BackgroundScheduler
    scheduler.add_job(check_for_reminders(), 'interval', minutes=5)
    scheduler.start()
