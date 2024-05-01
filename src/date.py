from datetime import date, time
import numpy as np

class Date:
    """
    Represents the date and time in which the exercise was completed.

    Attributes:
        date (datetime.date) : the date when the exercise was completed.
        time (datetime.time) : the time when the exercise started.

    """
    def __init__(self, year, month, day, h, min) :
        self.date = date(year=year, month=month, day=day)
        # Indicate the time to differenciate if in the same day the user did more than one workout.
        self.time = time(hour = h, minute = min)
    
    def print(self):
        return f'{self.date} - {self.time}'





