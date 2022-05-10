import pytest

from pytest import fixture
from services.database import *


@fixture
def db_up(data_a=DATA_SET_MAIN):
    db = Database(data_a)
    db.up_database()
    return db


def test_check_data_set_copy(data_a=DATA_SET_MAIN, data_b=DATA_SET_MAIN_COPY):
    assert len(data_a) == len(data_b)


def test_all_data_set_type(data_a=DATA_SET_MAIN, data_b=DATA_SET_MAIN_COPY, data_c=DATA_SET_ALTERNATIVE):
    all_data_sets = [data_a, data_b, data_c]
    for dataset in all_data_sets:
        assert type(dataset) is list


def test_add_user(db_up, username="newUser", password="12345"):
    db_up.add_user(username, password)
    assert username in db_up.database.keys()


def test_get_user(db_up, username="validUser"):
    assert type(db_up.database.get(username)) == User


def test_get_invalid_user(db_up, username="UserNotExpected"):
    with pytest.raises(Exception):
        assert username in db_up.database.keys()


def test_compare_user_password_matches(db_up, username="validUser", password="12345"):
    assert db_up.compare_password(username, password)


def test_compare_user_password_not_matches(db_up, username="validUser", password="invalidPassword"):
    with pytest.raises(Exception):
        assert db_up.compare_password(username, password)


def test_removing_existent_user(db_up, username="validUser"):
    assert db_up.remove_user(username) is None


def test_removing_not_existent_user(db_up, username="invalidUserExpected"):
    with pytest.raises(Exception):
        assert db_up.remove_user(username)


