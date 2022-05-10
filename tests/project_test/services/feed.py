from .user import *

class Feed():
    def __init__(self, host=User(), content=[]):
        self.host = host
        self.content = content
    
    def add_content(self, content):
        self.content.append(content)
    
    def get_host(self):
        return self.host