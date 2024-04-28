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


#Example of usage
if __name__ == '__main__':
    my_day = Date(2024, 4, 27, 6, 30)
    print(f'The exercise was done on the {my_day.date} at {my_day.time}.' )




