from .database import db

class users():
    """
    Provides abstraction of users, using the user class
    """


    def __init__(self):
        """
        Instantiates user object.
        """

        self.__database = instance = db()
        self.__db = instance.getInstance()
        self.__users = {}