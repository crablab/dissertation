# Written by myself previously, for the Team Project
import pymysql
from .singleton import Singleton

@Singleton
class db():
    """
    Encapsulation of database connection. 

    Creates a new connection upon instantiation and closes the connection upon destruction. 
    Whilst you're unlikely to need to access the class more than once you need to keep it in scope otherwise it will be auto-destructed by Python. 

    Example useage: 

    .. code-block:: python

        self.__database = instance = db.Instance()
        self.__db = instance.db
    """
    def __init__(self):
        self.db = pymysql.connect("localhost","registration","mgcMcYJ5jnrArYex?","registration", cursorclass=pymysql.cursors.DictCursor, charset='utf8', autocommit=True)

    def __del__(self):
        # Close connection on destruction
        self.db.close()