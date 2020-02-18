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
        # Instantiate class
        self.__database = instance = db()
        self.__db = instance.getInstance()
        self.__ph = PasswordHasher()
        self.__id_gen = cuid.CuidGenerator()
        self.__user = {"object": None, "authenticated": False}
    
    def check_login(self, password):
        """
        Checks password against current user, returning True if they match. 
        """

        # Take a copy to prevent TOCTOU
        user = self.__user
        
        if user['object'] == None:
            raise Exception("No user loaded")
        elif user["authenticated"] == True:
            return True
        
        # Check the password
        try:
            self.__ph.verify(user['object']['password'], password)
            user['authentciated'] = True
        except Exception as e:
            return False         
        
        self.__user = user
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
        """
        Finds a user by their email. If no matches returns False.
        """
        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM `users` WHERE `email` = %s;", email)

        count = cursor.rowcount

        if count == 1:
            return [count, cursor.fetchone()]
        elif count == 0:
            return [count]
        else:
            raise ValueError("Count of unexpected value", count)
    
    def __get_user_id(self, user_id):
        """
        Finds a user by their ID. If no matches returns False.
        """
        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM `users` WHERE `id` = %s;", user_id)

        count = cursor.rowcount

        if count == 1:
            return [count, cursor.fetchone()]
        elif count == 0:
            return [count]
        else:
            raise ValueError("Count of unexpected value", count)

    def load_user(self, user_id=None, email=None):
        """
        Loads a user into the object. 
        """
        self.__user = None

        if user_id != None and email == None:
            user = self.__get_user_id(user_id)
        elif email != None and user_id == None:
            user = self.__get_email(email)
        else:
            raise Exception("Ambiguous parameters")

        if user[0] == 1 and user[1] != None:
            self.__user = {"object": user[1], "authenticated": False}
            return True
        else:
            return False
    
    def get_user(self):
        """
        Returns the current user object.
        """
        try:
            if self.__user['object'] != None:
                return self.__user['object']
            else:
                return False
        except TypeError as e:
            return False
        
    def is_authenticated(self):
        pass

    def is_active(self):
        pass

    def is_anonymous(self):
        pass

    def get_id(self):
        pass