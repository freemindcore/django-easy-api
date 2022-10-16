from unittest.mock import Mock

from django.conf import settings

from easy_api.users.adapters import AccountAdapter, SocialAccountAdapter


def test_adapters(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(
            settings,
            "ACCOUNT_ALLOW_REGISTRATION",
            True
        )
        adapter = AccountAdapter()
        assert adapter.is_open_for_signup(request=Mock())

        m.setattr(
            settings,
            "ACCOUNT_ALLOW_REGISTRATION",
            False
        )
        adapter = SocialAccountAdapter()
        assert adapter.is_open_for_signup(request=Mock(), sociallogin=Mock()) is False
