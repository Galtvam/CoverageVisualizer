from .database import *


def password_is_valid(password):
    if len(password) < 5:
        return False
    return True


class Login():
    def __init__(self, data_set):
        self.db = self.db_create(data_set)

    def db_create(self, data_set):
        db = Database(data_set)
        db.up_database()
        return db

    def login_user(self, username, password):
        if self.db.get_user(username):
            if self.db.compare_password(username, password):
                return "Successfully logged in!"
            return "Password is incorrect, try another one!"
        return "This user does not exists!"

    def create_user(self, username, password):
        if self.db.user_exists(username) is False:
            if password_is_valid(password):
                self.db.add_user(username, password)
                return "User created with success!"
            return "The password must have at list 5 characters"
        return "This user already exists!"

