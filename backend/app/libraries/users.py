from .database import db
from . import user

class users():
    """
    Provides abstraction of users, using the user class
    """


    def __init__(self):
        """
        Instantiates user object.
        """

        self.__database = instance = db.Instance()
        self.__db = instance.db
        self.__users = {}
    
    @property
    def users(self):
        """
        :returns: user objects in a list.
        """
        users = {}

        for record in self.__users:
            uid = record['id']
            try:
                users[uid] = user.user()
                users[uid].load_user(user_id=uid)
            except Exception as e:
                return False
        
        return users

    def load_users(self):
        """
        Loads users into the class. 

        :returns: True/False depending on success.
        """

        cursor = self.__db.cursor()
        try:
            cursor.execute("SELECT `id` FROM `users`")
        except Exception as e:
            return False
        
        self.__users = cursor.fetchall()

        return True