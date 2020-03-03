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

        self.__database = instance = db.Instance()
        self.__db = instance.db
        self.__ph = PasswordHasher()
        self.__id_gen = cuid.CuidGenerator()
        self.__user = {"object": None, "authenticated": False}
    # PROPERTIES

    @property
    def is_authenticated(self):
        """
        Whether `check_login` has been completed in the current session. 

        Currently will always return True, due to flask_login issue.
        """
        return True
        #return self.__user['authenticated']

    @property
    def is_active(self):
        """
        Whether the user has been enabled or not. 
        """
        return self.__user['object']['enabled']

    @property
    def is_anonymous(self):
        """
        Always False - there are no anonymous users.
        """
        return False

    @property
    def get_permissions(self):
        """
        Returns the current user type. 
        """
        try:
            return self.__user['object']['type']
        except TypeError as e:
            return False
    
    def get_id(self):
        """
        Returns the current user ID. Psudo property for flask_wtf
        """
        try:
            return self.__user['object']['id']
        except TypeError as e:
            return False

    @property
    def id(self):
        return self.get_id()

    @property
    def name(self):
        return self.__user['object']['enabled']

    @property
    def email(self):
        return self.__user['object']['email']

    # METHODS

    def check_login(self, password):
        """
        Checks password against current user, returning True if they match. 

        :param password: The password the user has entered
        :returns: True on success, False on failed login
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
            user['authenticated'] = True
        except Exception as e:
            return False         
        
        self.__user = user
        return True
    
    def create_user(self, name, email, password, type):
        """
        Creates a new user in the database.

        :param name: User's name
        :param email: User's email
        :param password: User's password
        :param type: The type/role the user has 
        :returns: The user ID on success, False on failure
        :raises: PyMySQL exceptions if there is a database issue
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
        Finds a user by their email. 

        :param email: The email address to look for
        :returns: A list with the row count and user object as a dictionary 
        :returns: A list with the row count if there are no rows
        :raises: ValueError on multiple rows 
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
        Finds a user by their ID. 

        :param user_id: The user_id to look for
        :returns: A list with the row count and user object as a dictionary 
        :returns: A list with the row count if there are no rows
        :raises: ValueError on multiple rows 
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

        :param user_id: The user ID to load
        :param email: The email to load 
        :returns: True on success, False on failure
        :raises: Exception if both parameters are provided
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
    
    def __get_user(self):
        """
        Returns the current user object.

        :returns: Dictionary of the current user, or False if the user wasn't loaded 
        """
        try:
            if self.__user['object'] != None:
                return self.__user['object']
            else:
                return False
        except TypeError as e:
            return False