from services import user
import pytest
from services.user import User
from pytest import fixture


@fixture
def account_tester_real():
    return User("username", "password", 30, 60)


@fixture()
def account_tester_fake():
    return User("", 321, "30", "60")


def test_get_valid_username_of_user_account(account_tester_real):
    assert type(account_tester_real.username) is str and account_tester_real.username is not ""


def test_get_invalid_username_of_user_account(account_tester_fake):
    with pytest.raises(Exception):
        assert type(account_tester_fake.username) is not str or account_tester_fake.username is not ""


def test_get_valid_password_of_user_account(account_tester_real):
    assert type(account_tester_real.password) is str and len(account_tester_real.password) >= 5


def test_get_invalid_password_of_user_account(account_tester_fake):
    with pytest.raises(Exception):
        assert type(account_tester_fake.password) is not str and len(account_tester_fake.password) < 5


def test_get_valid_followers_of_user_account(account_tester_real):
    assert type(account_tester_real.followers) is int and account_tester_real.followers >= 0


def test_get_invalid_followers_of_user_account(account_tester_fake):
    with pytest.raises(Exception):
        assert type(account_tester_fake.followers) is str or account_tester_real.followers <= 0


def test_get_valid_following_of_user_account(account_tester_real):
    assert type(account_tester_real.followers) is int or account_tester_real.followers >= 0


def test_get_invalid_following_of_user_account(account_tester_fake):
    with pytest.raises(Exception):
        assert type(account_tester_fake.followers) is str or account_tester_real.followers <= 0


def test_user_class_type(account_tester_real):
    assert type(account_tester_real) is User
