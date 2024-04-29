class duration:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return f"{self.hours} hours, {self.minutes} minutes"

    def minutes_to_hours(self):
        return self.minutes / 60
    
    def hours_to_minutes(self):
        return self.hours * 60
    
    def display_minutes(self):
        return self.hours_to_minutes(self) + self.minutes
    
    def display_hours(self):
        return self.minutes_to_hours(self) + self.hours