from abc import ABC, abstractmethod

class Workout(ABC):
    """
    Abstract base class for a workout.

    Attributes:
        calories (Calories): Calories burnt during workout.
        date (Date): Date of the workout.
        distance (Distance): Distance covered during the workout.
        duration (Duration): The duration of the workout.
        rating (Rating): Rating of how the workout felt.
    """
    def __init__(self, calories, date, distance, duration, rating):
        self.calories = calories
        self.date = date
        self.distance = distance
        self.duration = duration
        self.rating = rating

    @abstractmethod
    def subclass_name(self):
        """
        Returns the name of the subclass (type of workout).
        """
        pass


class Running(Workout):
    """
    A running workout. See Workout for attributes.
    """
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Cycling(Workout):
    """
    A cycling workout. See Workout for attributes.
    """
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Strength(Workout):
    """
    A strength workout. See Workout for attributes.
    Distance is set to None for this type of Workout.
    """
    def __init__(self, calories, date, duration, rating):
        super().__init__(calories, date, None, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Swimming(Workout):
    """
    A swimming workout. See Workout for attributes.
    """
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Skiing(Workout):
    """
    A skiing workout. See Workout for attributes.
    """
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Walking(Workout):
    """
    A walking workout. See Workout for attributes.
    """
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Climbing(Workout):
    """
    A climbing workout. See Workout for attributes.
    Distance is set to None in this type of Workout.
    """
    def __init__(self, calories, date,  duration, rating):
        super().__init__(calories, date, None, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__

class Other(Workout):
    """
    A workout that is not running, cycling, strenght, swimming, skiing, walking and climbing. 
    See Workout for attributes.
    """
    def __init__(self, calories, date, distance, duration, rating):
        super().__init__(calories, date, distance, duration, rating)

    def subclass_name(self):
        return self.__class__.__name__
    