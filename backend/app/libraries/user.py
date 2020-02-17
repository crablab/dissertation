from .database import db
from argon2 import PasswordHasher
import datetime, cuid

class user():
    """
    Provides an abstraction of a user as an object. 
    """

    def __init__(self):
        """
        Instantiates user object.
        """
        # Instantiate Database
        self.__database = instance = db()
        self.__db = instance.getInstance()
        self.__ph = PasswordHasher()
        self.__id_gen = cuid.CuidGenerator()
    
    def check_login(self, email, password):
        """
        Checks the email and password, returning True if they match. 

        Note: this is a temporary function for testing.
        """
        user = self.__get_email(email)

        if user[0] == 0:
            return False
        elif user[0] > 1:
            raise ValueError("Duplicate users", email, user[0])
        
        # Check the password
        try:
            self.__ph.verify(user[1][0]['password'], password)
        except Exception as e:
            return False         
        
        return True
    
    def create_user(self, name, email, password, type):
        """
        Creates a new user in the database.
        """

        # Check for another email 
        if self.__get_email(email)[0] != 0:
            return False
    
        # Hash the password 
        hash = self.__ph.hash(password)

        # Generate an ID
        id = "user_" + self.__id_gen.cuid()

        enabled = 1

        # Insert into database
        cursor = self.__db.cursor()
        cursor.execute("INSERT INTO `users` (id, name, email, password, type, enabled) "
            "VALUES (%s, %s, %s, %s, %s, %s);", 
            (id, name, email, hash, type, enabled)
        )

        return id


    def __get_email(self, email):
        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM `users` WHERE `email` = %s;", email)

        count = cursor.rowcount

        if count > 0:
            return [count, cursor.fetchall()]
        elif count == 0:
            return [count]
        else:
            raise ValueError("Count of unexpected value", count)


