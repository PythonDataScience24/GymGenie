from datetime import date
import numpy as np

class Date:
    """
    Represents the date and time in which the exercise was completed.

    Attributes:
        date (datetime.date) : the date when the exercise was completed.
        time (datetime.time) : the time when the exercise started.

    """
    def __init__(self, year:int, month:int, day:int) :#h, min
        self.date_time = date(year=year, month=month, day=day)
    
#    def print(self):
#        return f'{self.date} - {self.time}'
    def print(self):
        return self.date_time




