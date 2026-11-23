from app.tasks.celery_app import celery_app

@celery_app.task
def send_notification(email: str, post_id: int):

    print(f"--- [CELERY] Уведомление для {email}: создан пост #{post_id} ---")