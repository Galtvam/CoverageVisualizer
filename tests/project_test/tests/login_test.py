from services.login import Login
from services.database import *

''' Login Test Suite: This specific suite cover the main functions and possibilities of a creation user '''


# Test if a user with a valid username and password is able to be logged
def test_login_valid_account_and_valid_password(data_set=DATA_SET_MAIN,
                                                username="validUser",
                                                password="12345"):
    assert Login(data_set).login_user(username, password) == "Successfully logged in!"


def test_login_invalid_account(data_set=DATA_SET_MAIN,
                                                  username="invalidUser",
                                                  password="12345"):
    assert Login(data_set).login_user(username, password) == "This user does not exists!"


def test_login_valid_account_and_invalid_password(data_set=DATA_SET_MAIN,
                                                  username="incorrectPasswordUser",
                                                  password="incorrectPassword"):
    assert Login(data_set).login_user(username, password) == "Password is incorrect, try another one!"


def test_create_new_account(data_set=DATA_SET_MAIN,
                            username="newUser",
                            password="12345"):
    assert Login(data_set).create_user(username, password) == "User created with success!"


def test_create_new_account_with_invalid_password(data_set=DATA_SET_MAIN,
                                                  username="newUser",
                                                  password=""):
    assert Login(data_set).create_user(username, password) == "The password must have at list 5 characters"


def test_create_new_account_if_already_user(data_set=DATA_SET_MAIN,
                                            username="validUser",
                                            password="12345"):
    assert Login(data_set).create_user(username, password) == "This user already exists!"
