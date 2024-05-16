class Duration:
    """
    Represents the duration of a workout.

    Attributes:
        hours (float): How many hours the workout lasted for.
        min (float): How many minutes the workout lasted for.
    """

    def __init__(self, hours=0, minutes=0):
        # Save duration as the total minutes spent.
        self.minutes = minutes + 60*hours

    def print(self):
        return self.short_str()

    def short_str(self):
        """
        Return duration in short string format. Example: "1h30".
        """
        return f"{self.get_hours()}h{self.get_minutes()}"

    def long_str(self):
        """
        Return duration in long string format. Example: "1 hours, 30 minutes".
        """
        return f"{self.get_hours()} hours, {self.get_minutes()} minutes"

    def get_hours(self):
        """
        Get the number of full hours of the duration.
        """
        return self.minutes // 60

    def get_minutes(self):
        """
        Get the number of residual minutes of the duration after the hours has been accounted for.
        """
        return self.minutes % 60


# Example usage
if __name__ == '__main__':
    my_duration = Duration(hours=1, minutes=30)

    # Print duration as short and long string
    print(my_duration.short_str())
    print(my_duration.long_str())

    # Get hours and minutes seperately
    print(my_duration.get_hours())
    print(my_duration.get_minutes())
