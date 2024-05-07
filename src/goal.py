from abc import ABC, abstractmethod
import numpy as np
import calories, date, distance, duration, workout

class Goal:
    """
    Abstract base class for a goal.

    Attributes:
        value: actual value that should be reached with this goal
        time_scale: number of days over which you want to achieve your goal (e.g. 7 to set a goal of )
        start_date (Date): date at which the goal was set
        end_date (Date): date by which the goal should be reached
        exercise (Workout): type of workout in which you want to achieve the goal. Default is None, to include all types of exercises.
    """
    def __init__(self, value: float, unit: str, time_scale: int, start_date: date.Date, end_date: date.Date, exercise = np.NaN):
        self.value = value
        self.unit = unit
        self.time_scale = time_scale
        self.start_date = start_date
        self.end_date = end_date
        self.exercise = exercise

    def __str__(self):
        """
        Returns a string representation for printing the Goal.
        """
        return f"Goal: {self.value} {self.unit} per {self.time_scale} days in exercise {self.exercise} \n Set on {self.start_date}, to reach until {self.end_date}"

    def get_start_date(self):
        return self.start_date
    
    def get_end_date(self):
        return self.end_date
    
    #for all attributes?

    def subclass_name(self):
        """
        Returns the name of the subclass (quantity for which the goal is set, i.e. calories, duration or distance).
        """
        return self.__class__.__name__

    
    
class CalorieGoal(Goal):
    """
    A goal set for calories. See Goal for attributes. The attribute value has to be of class Calories.
    """
    def __init__(self, value, time_scale, start_date, end_date, exercise = np.NaN):
        super().__init__(value, "kcal", time_scale, start_date, end_date, exercise)



class DistanceGoal(Goal):
    """
    A goal set for distances. See Goal for attributes. The attribute value has to be of class Distance.
    """
    def __init__(self, value, time_scale, start_date, end_date, exercise  = np.NaN):
        super().__init__(value, "km", time_scale, start_date, end_date, exercise)


class DurationGoal(Goal):
    """
    A goal set for duration of workouts. See Goal for attributes. The attribute value has to be of class Duration.
    """
    def __init__(self, value, time_scale, start_date, end_date, exercise = np.NaN):
        super().__init__(value, "min", time_scale, start_date, end_date, exercise)


if __name__ == "__main__":
    my_calories = calories.Calories(1000, "kcal")
    my_start_date = date.Date(2024, 5, 3, 0, 0)
    my_end_date = date.Date(2024, 10, 31, 0 ,0)
    my_distance = distance.Distance(20, "km")
    my_duration = duration.Duration(hours = 5)
    #think of a better way to get the type
    my_workout = workout.Running(my_calories, my_start_date, my_distance, my_duration, 5)

    my_duration_goal = DurationGoal(value = my_duration, time_scale = 7, start_date = my_start_date, end_date = my_end_date)
    my_duration_goal_running = DurationGoal(value = my_duration, time_scale = 14, start_date = my_start_date, end_date = my_end_date, exercise = my_workout.subclass_name())
    my_distance_goal = DistanceGoal(value = my_distance, time_scale = 7, start_date = my_start_date, end_date = my_end_date)
    my_calories_goal = CalorieGoal(value = my_calories, time_scale = 7, start_date = my_start_date, end_date = my_end_date)

    print(my_duration_goal)
    print(my_duration_goal.subclass_name())