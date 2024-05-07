
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


# Running pylint on the file src/workout.py

************* Module dataframe
dataframe.py:14:0: C0303: Trailing whitespace (trailing-whitespace)
dataframe.py:26:0: C0303: Trailing whitespace (trailing-whitespace)
dataframe.py:37:0: C0303: Trailing whitespace (trailing-whitespace)
dataframe.py:52:0: C0301: Line too long (107/100) (line-too-long)
dataframe.py:53:0: C0303: Trailing whitespace (trailing-whitespace)
dataframe.py:58:0: C0301: Line too long (239/100) (line-too-long)
dataframe.py:69:0: C0301: Line too long (110/100) (line-too-long)
dataframe.py:75:0: C0301: Line too long (220/100) (line-too-long)
dataframe.py:91:0: C0301: Line too long (145/100) (line-too-long)
dataframe.py:95:0: C0301: Line too long (129/100) (line-too-long)
dataframe.py:102:0: C0303: Trailing whitespace (trailing-whitespace)
dataframe.py:106:0: C0304: Final newline missing (missing-final-newline)
dataframe.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dataframe.py:3:0: C0410: Multiple imports on one line (goal, date, duration, workout, calories) (multiple-imports)
dataframe.py:54:26: W0621: Redefining name 'workout' from outer scope (line 3) (redefined-outer-name)
dataframe.py:71:23: W0621: Redefining name 'goal' from outer scope (line 3) (redefined-outer-name)
dataframe.py:88:20: E1121: Too many positional arguments for constructor call (too-many-function-args)
dataframe.py:89:18: E1121: Too many positional arguments for constructor call (too-many-function-args)
dataframe.py:2:0: C0411: standard import "from abc import ABC" should be placed before "import pandas as pd" (wrong-import-order)

-----------------------------------
Your code has been rated at 4.60/10

# Fixed Code:

"""
This module contains the Class Dataframe and subclasses for dataframes to store Workouts or Goals with specific column names. The data is stored in the data attribute. Methods allow to save the dataframe, print it, edit or delete entries, and add new entries (rows).
"""
from abc import ABC
import pandas as pd
import goal
import date
import duration
import workout
import calories

class Dataframe(ABC):
    """
    Abstract base class for a dataframe.

    Attributes:
        data: the Dataframe containing the entries as rows.
    """
    def __init__(self, column_names: list):
        self.data = pd.DataFrame(columns = column_names)

    def save_dataframe(self, path: str):
        """
        Save the dataframe to a specified path.
        """
        self.data.to_csv(path)

    def print_dataframe(self):
        """
        Print the dataframe contained in the data attribute of the object.
        """
        print(self.data)

    def edit_dataframe(self, column_name: str, row_idx: int, new_value):
        """
        Edit a specific cell of the dataframe.

        Args:
            column_name (str): Name of the column in which an entry should be edited.
            row_idx (int): Index of the row in which an entry should be edited.
            new_value: The value to be newly assigned to the specified entry.
        """
        self.data.loc[row_idx, column_name] = new_value

    def delete_entry(self, row_idx: int):
        """
        Delete a row (one entry) of the dataframe.
        
        Args:
        row_idx (int): Index of the row that should be removed.
        """
        self.data.drop(row_idx)

class WorkoutDataframe(Dataframe):
    """
    Dataframe  that contains the information about the workouts the user entered.
    """
    def __init__(self):
        super().__init__(column_names =
                        ["activity", "date", "duration", "distance", "calories", "rating"])

    def add_workout(self, new_entry: workout.Workout):
        """
        Add a new workout as a new row to the dataframe.
        """
        self.data = pd.concat([self.data, pd.DataFrame({"activity":[new_entry.subclass_name()],
                                                        "date":[new_entry.date],
                                                        "duration":[new_entry.duration],
                                                        "distance":[new_entry.distance],
                                                        "calories":[new_entry.calories],
                                                        "rating":[new_entry.rating]})])
        #make sure duplicated entries are not possible
        if sum(self.data.duplicated()) > 0:
            print("This workout is already present in the table, the second entry will be dropped.")
            self.data.drop_duplicates(inplace = True)

class GoalDataframe(Dataframe):
    """
    Dataframe that contains the information about the goals the user set.
    """
    def __init__(self):
        super().__init__(column_names =
                         ["value", "unit", "time_scale", "start_date", "end_date", "exercise"])

    def add_goal(self, new_entry: goal.Goal):
        """
        Add a new goal as a new row to the dataframe.
        """
        self.data = pd.concat([self.data, pd.DataFrame({"value":[new_entry.value],
                                                        "unit":[new_entry.unit],
                                                        "time_scale":[new_entry.time_scale],
                                                        "start_date":[new_entry.start_date],
                                                        "end_date":[new_entry.end_date], 
                                                        "exercise":[new_entry.exercise]})])
        #make sure duplicated entries are not possible
        if sum(self.data.duplicated()) > 0:
            print("This goal is already present in the table, the second entry will be dropped.")
            self.data.drop_duplicates(inplace = True)

if __name__ == "__main__":
    my_workout_df = WorkoutDataframe()
    my_workout_df.print_dataframe()
    my_goals_df = GoalDataframe()
    my_goals_df.print_dataframe()

    #create a workout and a goal to store in the dataframe
    my_start_date = date.Date(2024, 5, 3, 0, 0)
    my_end_date = date.Date(2024, 10, 31, 0 ,0)
    my_duration = duration.Duration(hours = 5)
    my_duration_goal = goal.DurationGoal(value = my_duration, time_scale = 7,
                                          start_date = my_start_date.print(),
                                          end_date = my_end_date.print())
    my_duration = duration.Duration(minutes = 90)
    my_calories = calories.Calories(230, unit = "kcal")
    my_workout = workout.Climbing(my_calories, my_start_date, my_duration, 7)
    my_duration_goal = goal.DurationGoal(value = my_duration, time_scale = 7,
                                         start_date = my_start_date,
                                         end_date = my_end_date)

    #add the entries to the dataframe
    my_workout_df.add_workout(my_workout)
    my_workout_df.print_dataframe()
    my_goals_df.add_goal(my_duration_goal)
    my_goals_df.print_dataframe()

    #check some other functions of the Parent Class
    my_goals_df.add_goal(my_duration_goal)
    my_goals_df.edit_dataframe("value", 0, duration.Duration(minutes = 120))
    my_goals_df.print_dataframe()
