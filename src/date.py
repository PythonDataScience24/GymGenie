from datetime import date
import numpy as np

class Date:
    """
    Represents the date and time in which the exercise was completed.

    Attributes:
        date_time (datetime.date) : the date when the exercise was completed.
    """
    def __init__(self, year: int, month: int, day: int) :
        self.date_time = date(year=year, month=month, day=day)
    

    def print(self):
        return self.date_time




