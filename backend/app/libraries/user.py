from .database import db
from argon2 import PasswordHasher
import datetime

class user():
    """
    Provides an abstraction of a user as an object. 
    """

    def __init__(self):
        # Instantiate Database
        self.__database = instance = db()
        self.__db = instance.getInstance()
    
    def check_login(self, email, password):
        cursor.execute("SELECT * FROM `users` WHERE `email` = %s;", email)
        if cursor.rowcount == 1:
            user = cursor.fetchone()
        elif cursor.rowcount == 0:
            return False
        else:
            raise Exception("Duplicate users")
        
        # Check the password
        try:
            ph.verify(user['password'], password)
        except Exception as e:
            return False 
        
        return True