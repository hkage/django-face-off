import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db
def test_db_access():
    User.objects.all()
    assert 1==1
