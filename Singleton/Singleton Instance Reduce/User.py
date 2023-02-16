class User(object):

    __instance = None

    # new is modify a instance example a = A()
    def __new__(cls): # cls = self>>Class
        if User.__instance is None:
            print("Creating new OBj")
            User.__instance = object.__new__(cls)
