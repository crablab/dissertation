import pymysql

class db():
    """
    Encapsulation of database connection. 

    Creates a new connection upon instantiation and closes the connection upon destruction. 
    Whilst you're unlikely to need to access the class more than once you need to keep it in scope otherwise it will be auto-destructed by Python. 

    Example useage: 

    .. code-block:: python

        self.__databaseClass = db()
        self.__connectionObject = databaseClass.getInstance()
    """
    def __init__(self):
        self.__db = pymysql.connect("178.62.61.46","teamproject","a6ErM22GHr36CUHF","teamproject", cursorclass=pymysql.cursors.DictCursor, charset='utf8', autocommit=True)

    def getInstance(self):
        """
        Getter for connection instance. 

        :returns: PyMySQL connection object
        """
        return self.__db

    def __del__(self):
        # Close connection on destruction
        self.__db.close()