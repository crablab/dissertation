from .database import db
from pymysql import IntegrityError
from datetime import datetime
import cuid
from . import lectures

class allocation():
    """
    Abstracts the allocation of a student to a lecture.
    """

    def __init__(self):
        """ 
        Sets up the class and database objects.
        """
        self.__database = instance = db.Instance()
        self.__db = instance.db
        self.__id_gen = cuid.CuidGenerator()
        self.__allocation = {}

    # Properties 
    @property
    def id(self):
        print(self.__allocation)
        return self.__allocation['id']

    @property
    def course(self):
        return self.__allocation['course']

    @property
    def user(self):
        return self.__allocation['user']

    @property
    def allocated(self):
        return self.__allocation['allocated']

    # Methods

    def allocate(self, user, course):
        """
        Allocates a user to a course. 

        :param user: User ID of user to be allocated. 
        :param course: Course code of lectures to be assigned. 
        """

        # Generate an ID
        id = "allocation_" + self.__id_gen.cuid()

        # Insert into database
        cursor = self.__db.cursor()
        try:
            cursor.execute("INSERT INTO `allocations` (id, course, user) "
                "VALUES (%s, %s, %s);", 
                (id, course, user)
            )
        except IntegrityError as e:
            # Catch foreign key constraint issues 
            return False


        # Autoload into class 
        self.load_allocation(id)
        
        return id

    def load_allocation(self, allocation_id):
        """
        Gets a given allocation. 

        :param id: The allocation ID to fetch an allocation for. 
        """

        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM `allocations` WHERE `id` = %s;", allocation_id)

        count = cursor.rowcount

        if count == 1:
            self.__allocation = cursor.fetchone()
        else:
            raise ValueError("Count of unexpected value", count)

        return True