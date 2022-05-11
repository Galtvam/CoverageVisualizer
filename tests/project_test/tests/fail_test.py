from services.database import *

def test_fail():
    assert True == False

def test_fail_2():
    db = Database(data_set=['user_1', 'user_2'])
    assert True == False