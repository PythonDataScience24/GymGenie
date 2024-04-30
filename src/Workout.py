from abc import ABC, abstractmethod

class Workout(ABC):
    def __init__(self, calories, date, distance, duration, rating):
        self.calories = calories
        self.date = date
        self.distance = distance
        self.duration = duration
        self.rating = rating


    @abstractmethod
    def subclass_name(self):
        pass


class Running(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Cycling(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Strength(Workout):
    def __init__(self, calories, date, duration, rating):
        super().__init__(calories, date, None, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Swimming(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Skiing(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Walking(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Climbing(Workout):
    def __init__(self, calories, date,  duration, rating):
        super().__init__(calories, date, None, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Other(Workout):
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

