from django.contrib.auth import get_user_model

from config import celery_app

User = get_user_model()


@celery_app.task(bind=True)
def users_count(self):
    return User.objects.count()
