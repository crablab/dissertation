from .database import db
from datetime import datetime
import cuid

class lecture():
    """
    Abstraction of a lecture/class. 
    """

    def __init__(self):
        """ 
        Sets up the class and database objects.
        """
        self.__database = instance = db()
        self.__db = instance.getInstance()
        self.__id_gen = cuid.CuidGenerator()
        self.__lecture = {}

    # Properties
    @property
    def id(self):
        return self.__lecture['id']

    @property
    def course(self):
        return self.__lecture['course']
    
    @property
    def time(self):
        return self.__lecture['datetime']
    
    # Methods 
    def load_lecture(self, lecture_id):
        """
        Loads a given lecture ID into the object.

        :param lecture_id: The unique ID of the lecture to load
        :returns: True on success 
        :raises: ValueError if row count is 0 or > 1
        """

        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM `lectures` WHERE `id` = %s;", lecture_id)

        count = cursor.rowcount

        if count == 1:
            self.__lecture = cursor.fetchone()
        else:
            raise ValueError("Count of unexpected value", count)

        return True

    def create_lecture(self, course, lecture_datetime):
        """
        Creates a lecture. 

        :param course: The course code to create the lecture for.
        :param datetime: The datetime of the lecture.
        :returns: Lecture ID on success.
        :raises: ValueError if datetime is not a datetime object.
        :raises: Value Error if datetime is now or in the past.
        """

        # Check the date is a datetime object
        if not isinstance(lecture_datetime, datetime):
            raise ValueError("Lecture datetime not a valid Datetime object")

        # Check we're not creating a lecture in the past            
        if lecture_datetime <= datetime.now(): 
            raise ValueError("Lecture cannot be in the past")

        # Generate an ID
        id = "lecture_" + self.__id_gen.cuid()

        cursor = self.__db.cursor()
        cursor.execute("INSERT INTO `lectures` (id, course, datetime)"
            "VALUES (%s, %s, %s);", 
            (id, course, lecture_datetime)
        )

        # Load the newly created lecture 
        self.load_lecture(id)

        return id

    def delete_lecture(self):
        """
        Deletes a lecture. 

        :returns: True on success 
        :raises: ValueError when lecture not loaded
        :raises: IntegrityError where deletion would violate constraints
        """
        if "id" not in self.__lecture:
            raise ValueError("Not lecture loaded")

        cursor = self.__db.cursor()
        cursor.execute("DELETE FROM `lectures` WHERE `id` = %s;", 
            (self.id)
        )

        return True
