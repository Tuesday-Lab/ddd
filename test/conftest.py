import uuid
import os

# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings.test")

import pytest


# def pytest_configure(config):
#     django.setup()


@pytest.fixture
def test_password():
    return 'strong-test-pass'


@pytest.fixture(autouse=True)
def use_dummy_cache_backend(settings):
    settings.CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    }


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            _uuid = str(uuid.uuid4())
            kwargs['name'] = _uuid
            kwargs['email'] = "f{_uuid}@test.com"
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture
def admin_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'name' not in kwargs:
            _uuid = str(uuid.uuid4())
            kwargs['name'] = _uuid
            kwargs['email'] = "f{_uuid}@test.com"
        return django_user_model.objects.create_superuser(**kwargs)

    return make_user


@pytest.fixture
def auto_login_user(db, client, create_user, admin_user, test_password):
    def make_auto_login(user=None, is_admin=False):
        if user is None:
            if is_admin:
                user = admin_user()
            else:
                user = create_user()
        client.login(email=user.email, password=test_password)
        return client, user

    return make_auto_login
