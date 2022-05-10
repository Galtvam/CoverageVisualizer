from .user import *

class Database():
    def __init__(self, data_set):
        self.data_set = data_set
        self.database = {}

    def up_database(self):
        for user in self.data_set:
            this_user = User(user['Username'], user['Password'], user['Followers'], user['Following'])
            self.database[this_user.get_username()] = this_user
        return self.data_set

    def add_user(self, username, password):
        new_user = User(username, password)
        self.database[new_user.get_username()] = new_user

    def get_user(self, username):
        if self.user_exists(username):
            return True
        return False

    def compare_password(self, username, password):
        if self.get_password(username) == password:
            return True
        return False

    def remove_user(self, username):
        if self.user_exists(username):
            del self.database[username]

    def user_exists(self, key):
        if self.database.get(key) is not None:
            return True
        return False

    def get_password(self, username):
        if self.user_exists(username):
            return self.database.get(username).get_password()

#datasets
DATA_SET_MAIN = [
    {
        "Username": "validUser",
        "Password": "12345",
        "Followers": 100,
        "Following": 1,
    },
    {
        "Username": "validUser2",
        "Password": "12345",
        "Followers": 321,
        "Following": 2,
    },
    {
        "Username": "incorrectPasswordUser",
        "Password": "12345",
        "Followers": 23,
        "Following": 23,
    }
]
DATA_SET_ALTERNATIVE = [
    {
        "Username": "validUser123",
        "Password": "12345",
        "Followers": 100,
        "Following": 1,
    },
    {
        "Username": "validUser321",
        "Password": "12345",
        "Followers": 100,
        "Following": 1,
    },
    {
        "Username": "incorrectUser",
        "Password": "nopassword",
        "Followers": 100,
        "Following": 1,
    }
]
DATA_SET_MAIN_COPY = [
    {
        "Username": "validUser",
        "Password": "123456",
        "Followers": 100,
        "Following": 1,
    },
    {
        "Username": "validUser2",
        "Password": "12345",
        "Followers": 321,
        "Following": 2,
    },
    {
        "Username": "incorrectPasswordUser",
        "Password": "incorrectPassword",
        "Followers": 23,
        "Following": 23,
    }
]




