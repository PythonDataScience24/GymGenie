from abc import ABC

class Workout(ABC):
    def __init__(self, calories, date, distance, duration, rating):
        self.calories = calories
        self.date = date
        self.distance = distance
        self.duration = duration
        self.rating = rating


    #@abstractmethod
    #def role(self):
    #    pass

class Running(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super.__init__(self, calories, date, distance, duration, rating)

class Cycling(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super.__init__(self, calories, date, distance, duration, rating)

class Strength(Workout):
    def __init__(self, calories, date, duration, rating):
        super.__init__(self, calories, date, None, duration, rating)

class Swimming(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super.__init__(self, calories, date, distance, duration, rating)

class Skiing(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super.__init__(self, calories, date, distance, duration, rating)

class Walking(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super.__init__(self, calories, date, distance, duration, rating)

class Climbing(Workout):
    def __init__(self, calories, date,  duration, rating):
        super.__init__(self, calories, date, None, duration, rating)

class Other(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super.__init__(self, calories, date, distance, duration, rating)

    
