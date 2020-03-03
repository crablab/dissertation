from .database import db
from datetime import datetime
from . import lecture

class lectures():
    """
    Abstraction of a collection of lectures.
    """

    def __init__(self):
        """ 
        Sets up the class and database objects.
        """
        self.__database = instance = db.Instance()
        self.__db = instance.db
        self.__lectures = {}

    # Properties
    @property
    def lectures(self):
        """
        :returns: lecture objects in a list.
        """
        lectures = {}

        for record in self.__lectures:
            lid = record['id']
            try:
                lectures[lid] = lecture.lecture()
                lectures[lid].load_lecture(lid)
            except Exception as e:
                return False
        
        return lectures

    # Methods 
    def load_lectures(self, course=None, time=None):
        """
        Loads all lectures. Potentially expensive. 

        :returns: True/False depending on success
        """
        # Based on this StackOverflow: https://stackoverflow.com/a/49688389/3525352
        # DECLARATIONS
        cursor = self.__db.cursor()
        sql = ["SELECT `id` FROM `lectures`"]
        args = []

        def add_arg(name, value):
            if value:
                # Base case
                if len(sql) == 1:
                    sql.append("WHERE")
                    sql.append('`{}` = %s'.format(name))
                else:
                    sql.append('AND `{}` = %s'.format(name))

                args.append(value)

        # PROCEDURE
        if course != None:
            add_arg('course', course)
        if time != None:
            if isinstance(time, datetime):
                add_arg('datetime', time)
            else:
                raise ValueError("Lecture datetime not a valid Datetime object")
        
        string = ' '.join(sql)
        
        cursor.execute(string, args)
        self.__lectures = cursor.fetchall()

        return True