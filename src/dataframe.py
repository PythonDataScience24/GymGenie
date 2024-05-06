import pandas as pd
from abc import ABC, abstractmethod
import goal, date, duration, workout, calories

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
        super().__init__(column_names = ["activity", "date", "duration", "distance", "calories", "rating"])
   
    def add_workout(self, workout: workout.Workout):
        """
        Add a new workout as a new row to the dataframe.
        """
        self.data = pd.concat([self.data, pd.DataFrame({"activity":[workout.subclass_name()], "date":[workout.date], "duration":[workout.duration], "distance":[workout.distance], "calories":[workout.calories], "rating":[workout.rating]})])
        #make sure duplicated entries are not possible
        if sum(self.data.duplicated()) > 0:
            print("This workout is already present in the table, the second entry will be dropped.")
            self.data.drop_duplicates(inplace = True)

class GoalDataframe(Dataframe):
    """
    Dataframe that contains the information about the goals the user set.
    """
    def __init__(self):
        super().__init__(column_names = ["value", "unit", "time_scale", "start_date", "end_date", "exercise"])

    def add_goal(self, goal: goal.Goal):
        """
        Add a new goal as a new row to the dataframe.
        """
        self.data = pd.concat([self.data, pd.DataFrame({"value":[goal.value], "unit":[goal.unit], "time_scale":[goal.time_scale], "start_date":[goal.start_date], "end_date":[goal.end_date], "exercise":[goal.exercise]})])
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
    my_duration = duration.Duration(minutes = 90)
    my_calories = calories.Calories(230, unit = "kcal")
    my_workout = workout.Climbing(my_calories, my_start_date, my_duration, 7)
    my_duration_goal = goal.DurationGoal(value = my_duration, time_scale = 7, start_date = my_start_date, end_date = my_end_date)

    #add the entries to the dataframe
    my_workout_df.add_workout(my_workout)
    my_workout_df.print_dataframe()
    my_goals_df.add_goal(my_duration_goal)
    my_goals_df.print_dataframe()
    
    #check some other functions of the Parent Class
    my_goals_df.add_goal(my_duration_goal)
    my_goals_df.edit_dataframe("value", 0, duration.Duration(minutes = 120))
    my_goals_df.print_dataframe()