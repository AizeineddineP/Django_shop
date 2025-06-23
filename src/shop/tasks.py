from celery import shared_task
from datetime import datetime

@shared_task
def send_welcome_email(user_id):
    print(f"[{datetime.now()}] Email sent to user {user_id}")

@shared_task
def every_3min_40s():
    print(f"[{datetime.now()}] Task: every 3 min 40 sec")

@shared_task(bind=True)
def three_times_between_19_and_21(self):
    print(f"[{datetime.now()}] Task: between 19–21h")