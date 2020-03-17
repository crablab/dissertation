from .database import db
from pymysql import IntegrityError
from datetime import datetime
from . import allocation

class allocations():
    """
    Abstracts multiple instances of allocations eg. for a student.
    """

    def __init__(self):
        """
        Instantiates allocations object.
        """

        self.__database = instance = db.Instance()
        self.__db = instance.db
        self.__allocations = {}
    
    @property
    def allocations(self):
        """
        :returns: allocation objects in a list.
        """
        allocations = {}

        for record in self.__allocations:
            aid = record['id']
            try:
                allocations[aid] = allocation.allocation()
                allocations[aid].load_allocation(aid)
            except Exception as e:
                return False
        
        return allocations

    def load_allocations(self):
        """
        Loads allocations into the class. 

        :returns: True/False depending on success.
        """

        cursor = self.__db.cursor()
        try:
            cursor.execute("SELECT `id` FROM `allocations`")
        except Exception as e:
            return False
        
        self.__allocations = cursor.fetchall()

        return True