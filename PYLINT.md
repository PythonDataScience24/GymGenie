
# Running pylint on the file src/workout.py

************* Module workout
***src\workout.py:23:0: C0303: Trailing whitespace (trailing-whitespace)***
***src\workout.py:29:0: C0303: Trailing whitespace (trailing-whitespace)***
***src\workout.py:35:0: C0303: Trailing whitespace (trailing-whitespace)***
***src\workout.py:41:0: C0303: Trailing whitespace (trailing-whitespace)***
***src\workout.py:47:0: C0303: Trailing whitespace (trailing-whitespace)***
***src\workout.py:1:0: C0114: Missing module docstring (missing-module-docstring)***
src\workout.py:17:4: R0913: Too many arguments (6/5) (too-many-arguments)
***src\workout.py:65:4: W0246: Useless parent or super() delegation in method '__init__' (useless-parent-delegation)***
src\workout.py:65:4: R0913: Too many arguments (6/5) (too-many-arguments)
***src\workout.py:72:4: W0246: Useless parent or super() delegation in method '__init__' (useless-parent-delegation)***
src\workout.py:72:4: R0913: Too many arguments (6/5) (too-many-arguments)
***src\workout.py:87:4: W0246: Useless parent or super() delegation in method '__init__' (useless-parent-delegation)***
src\workout.py:87:4: R0913: Too many arguments (6/5) (too-many-arguments)
***src\workout.py:94:4: W0246: Useless parent or super() delegation in method '__init__' (useless-parent-delegation)***
src\workout.py:94:4: R0913: Too many arguments (6/5) (too-many-arguments)
***src\workout.py:101:4: W0246: Useless parent or super() delegation in method '__init__' (useless-parent-delegation)***
src\workout.py:101:4: R0913: Too many arguments (6/5) (too-many-arguments)
***src\workout.py:117:4: W0246: Useless parent or super() delegation in method '__init__' (useless-parent-delegation)***
src\workout.py:117:4: R0913: Too many arguments (6/5) (too-many-arguments)
***src\workout.py:1:0: W0611: Unused abstractmethod imported from abc (unused-import)***

-----------------------------------
Your code has been rated at 5.56/10

# Fixed code:

""""
This module contains the Class Workout and subclasses for different types of exercises (Running, Cycling, Strength, Swimming, Skiing, Walking, Climbing, Other). Each object has attributes for calories used, date of the exercise, distance covered (if applicable to the type of workout), duration and personal rating of the workout. The methods allow to retrieve each individual attribute of the Workout object.
"""

from abc import ABC
import numpy as np

#Test

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

    def get_calories(self):
        """
        Return the attribute of calories
        """
        return self.calories

    def get_date(self):
        """
        Return the attribute of date
        """
        return self.date

    def get_distance(self):
        """
        Return the attribute of distance
        """
        return self.distance

    def get_duration(self):
        """
        Return the attribute of duration
        """
        return self.duration

    def get_rating(self):
        """
        Return the attribute of rating
        """
        return self.rating

    def subclass_name(self):
        """
        Returns the name of the subclass (type of workout).
        """
        return self.__class__.__name__


class Running(Workout):
    """
    A running workout. See Workout for attributes.
    """

class Cycling(Workout):
    """
    A cycling workout. See Workout for attributes.
    """

class Strength(Workout):
    """
    A strength workout. See Workout for attributes.
    Distance is set to None for this type of Workout.
    """
    def __init__(self, calories, date, duration, rating):
        super().__init__(calories, date, np.NaN, duration, rating)

class Swimming(Workout):
    """
    A swimming workout. See Workout for attributes.
    """

class Skiing(Workout):
    """
    A skiing workout. See Workout for attributes.
    """

class Walking(Workout):
    """
    A walking workout. See Workout for attributes.
    """

class Climbing(Workout):
    """
    A climbing workout. See Workout for attributes.
    Distance is set to None in this type of Workout.
    """
    def __init__(self, calories, date,  duration, rating):
        super().__init__(calories, date, np.NaN, duration, rating)

class Other(Workout):
    """
    A workout that is not running, cycling, strenght, swimming, skiing, walking or climbing. 
    See Workout for attributes.
    """