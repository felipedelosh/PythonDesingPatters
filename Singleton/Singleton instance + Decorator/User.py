def singleton(cls):
    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls]= cls(*args, **kwargs)
        
        return instances[cls]

    return wrap

@singleton
class User(object):
    def __init__(self, username) -> None:
        self.username = username

@singleton
class Admin():
    pass

