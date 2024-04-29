from datetime import date, time

class Date:
    """
    Represents the date and time in which the exercise was completed.

    Attributes:
        date (datetime.date) : the date when the exercise was completed.
        time (datetime.time) : the time when the exercise started.

    """
    def __init__(self, year, month, day, h, min) :
        self.date = date(year=year, month=month, day=day)
        self.time = time(hour = h, minute = min)
    
    def print(self):
        return f'{self.date} - {self.time}'





