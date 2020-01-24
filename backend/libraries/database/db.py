from sqlalchemy import create_engine

class database():
    """
    Provides a singleton adaptor to the underlying ORM and database connectivity via SQLAlchemy.
    """
    # In production, these would be passed in as environment variables
    __host = "localhost"
    __username  = "root"
    __password = "q9LQ44?vNa2fM?[66s{I"
    __port = "3306"
    __database = "registration"

    def __init__(self):
        # Create the database connection 
        self.__conn = create_engine(
            'mysql+pymysql://' + self.__username + 
            ':' + self.__password + 
            '@' + self.__host + 
            ':' + self.__port + 
            '/' + self.__database + '').connect()
    
    def check_connection(self):
        return self.__conn.execute("SHOW STATUS;")