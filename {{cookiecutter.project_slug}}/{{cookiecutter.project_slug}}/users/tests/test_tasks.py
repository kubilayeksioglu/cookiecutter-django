import pytest
from celery.result import EagerResult


from {{ cookiecutter.project_slug }}.users.tasks import users_count
from {{ cookiecutter.project_slug }}.users.tests.factories import UserFactory


@pytest.mark.django_db
def test_user_count(settings):
    UserFactory.create_batch(3)
    settings.CELERY_TASK_ALWAYS_EAGER = True
    task_result = users_count.delay()
    assert isinstance(task_result, EagerResult)
    assert task_result.result == 3
