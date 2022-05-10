class User():
    def __init__(self, username, password, followers=0, following=0):
        self.username = username
        self.password = password
        self.followers = int(followers)
        self.following = int(following)

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following

    def set_followers(self):
        self.followers = 0
        
    def __class__(self):
        return User
