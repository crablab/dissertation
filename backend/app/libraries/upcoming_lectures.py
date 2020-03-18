from .database import db
from pymysql import IntegrityError
from datetime import datetime
from operator import attrgetter
from . import allocations, lectures

class upcoming_lectures(lectures.lectures):
    """
    Extends lectures to provide next and upcoming views per user.
    """

    def __init__(self):
        """
        Instantiate the class
        """
        # Instantiates the inherited class
        super().__init__()

        self.__allocations = allocations.allocations()
        self.__lectures = lectures.lectures()
        self.__upcoming = []

    # Properties
    @property
    def get_upcoming(self):
        # Sort lectures 
        sort = sorted(self.__upcoming, key=attrgetter('time'))

        return sort

    # Methods

    def load_upcoming(self, user):
        # Prevent TOCTOU bugs
        now = datetime.now()

        self.__allocations.load_allocations(user)
        allocations = self.__allocations.allocations

        for key in allocations:
            # For each allocation, load the lecture series
            print(self.__lectures.load_lectures(course=allocations[key].course))
            lectures = self.__lectures.lectures

            # For each lecture append if it's in the future
            for key in lectures:
                if lectures[key].time > now:
                    self.__upcoming.append(lectures[key])

        return True


        
        
        