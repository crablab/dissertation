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
            print(record)
            try:
                allocations[aid] = allocation.allocation()
                allocations[aid].load_allocation(aid)
            except Exception as e:
                return False
        
        print(allocations)
        return allocations

    def load_allocations(self, user=None):
        """
        Loads all allocations

        :returns: True/False depending on success
        """
        # Based on this StackOverflow: https://stackoverflow.com/a/49688389/3525352
        # DECLARATIONS
        cursor = self.__db.cursor()
        sql = ["SELECT `id` FROM `allocations`"]
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
        if user != None:
            add_arg('user', user)
        
        string = ' '.join(sql)
        
        cursor.execute(string, args)
        self.__allocations = cursor.fetchall()

        return True