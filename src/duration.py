class Duration:
    def __init__(self, hours=0, minutes=0):
        self.minutes = minutes + 60*hours

    def __str__(self):
        return self.short_str()
        # return self.long_str()    

    def short_str(self):     
            return f"{self.get_hours()}h{self.get_minutes()}"
    
    def long_str(self):     
        return f"{self.get_hours()} hours, {self.get_minutes()} minutes"

    def get_hours(self):
        return self.minutes // 60
    
    def get_minutes(self):
        return self.minutes % 60
