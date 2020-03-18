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
        self.__lectures = []

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
    
    def load_distinct_courses(self):
        """
        Special snowflake method to return distinct courses.

        This returns single lecture IDs for each course, but the instance returned is not deterministic. 

        :returns: True/False depending on success
        """
        cursor = self.__db.cursor()
        cursor.execute("SELECT DISTINCT `id`, `course` FROM `lectures`;")

        lectures = cursor.fetchall()

        # Iterate to remove duplicates (which doesn't matter for the callers of this)
        dedupe = []

        for key, record in enumerate(lectures):
            if record['course'] in dedupe:
                # Ignore, already deduplicated
                pass
            else:
                # Push to the class variable and add to list of "seen" courses
                self.__lectures.append(lectures[key])
                dedupe.append(record['course'])

        return True