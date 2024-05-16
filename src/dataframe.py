"""
This module contains the Class Dataframe and subclasses for dataframes to store Workouts or Goals with specific column names. The data is stored in the data attribute. Methods allow to save the dataframe, print it, edit or delete entries, and add new entries (rows).
"""
from abc import ABC
import pandas as pd
from goal import Goal, DurationGoal
from date import Date
from duration import Duration
from workout import Workout,Climbing
from calories import Calories

class Dataframe(ABC):
    """
    Abstract base class for a dataframe.

    Attributes:
        data: the Dataframe containing the entries as rows.
    """

    def __init__(self, column_names: list, *args, **kwargs):
        pd.DataFrame.__init__(self,*args,**kwargs)
        self.data = pd.DataFrame(columns=column_names)

    def save_to_csv(self, path: str):
        """
        Save the dataframe to a specified path.
        """
        self.data.to_csv(path, encoding='utf-8', index=False)
    
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
        self.data.drop(inplace=True,index=row_idx)
        
    def read_from_csv(self, path: str):
        """
        Read data from a csv file and store it as a dataframe in the data attribute.
        """
        input_data = pd.read_csv(path)
        self.data = input_data


    def extract_date(self,date:str):
        """
        Transform the date string in a Date object
        """
        info =  date.split('-')

        return Date(int(info[0]), int(info[1]), int(info[2])).print()
class WorkoutDataframe(Dataframe):
    """
    Dataframe  that contains the information about the workouts the user entered.
    """

    def __init__(self):
        super().__init__(column_names=[
            "activity", "date", "duration", "distance", "calories", "rating"])

    def add_workout(self, new_entry: Workout):
        """
        Add a new workout as a new row to the dataframe.
        """
        self.data = pd.concat([self.data, pd.DataFrame({"activity": [new_entry.subclass_name()],
                                                        "date": [new_entry.date],
                                                        "duration": [new_entry.duration],
                                                        "distance": [new_entry.distance],
                                                        "calories": [new_entry.calories],
                                                        "rating": [new_entry.rating]})], ignore_index=True)
        # make sure duplicated entries are not possible
        if sum(self.data.duplicated()) > 0:
            print(
                "This workout is already present in the table, the second entry will be dropped.")
            self.data.drop_duplicates(inplace=True)

    def plot_dataframe(self):
        """
        Transform the data of the dataframe to use it for plotting
        """
        #print(self.data)
        self.data['date'] = self.data['date'].apply(self.extract_date)
        self.data['duration'] = self.data['duration'].apply(self.extract_duration)
        self.data['distance'] = self.data['distance'].apply(self.extract_distance)
        self.data['calories'] = self.data['calories'].apply(self.extract_calories)
        self.data['rating'] = self.data['rating'].apply(self.extract_rating)


    def extract_duration(self,duration:str):
        """
        Transforms the duration string in a float for plotting.
        """
        info = duration.split('h')
        
        return float(int(info[0]) * 60 +  int(info[1]))
    
    def extract_distance(self,distance:str):
        """
        Transforms the distance string in a float for plotting.
        """
        info = distance.split(" ")

        return float(info[0])
    
    def extract_calories(self,calories:str):
        """
        Transforms the calories string in a float for plotting.
        """
        info = calories.split(" ")

        return float(info[0])
    
    def extract_rating(self,ratings:str):
        """
        Transforms the rating string in a interger for plotting.
        """
        return int(ratings)
    def test_values(self):
        """
        Test that the dataframe doesn't contains unrealistic values
        """
        index = self.data.index[(self.data['date'] == Date(1,1,1).print()) & (self.data['duration'] == Duration(0,0).print()) &
                                (self.data['distance'] == Distance(0,"km").print()) & (self.data['calories'] == Calories(0,'kcal').print()) &
                                (self.data['rating'] == Rating(1).print())].to_list()
        print(index)
        if len(index) != 0:
            # drop all the lines with unrealist values
            self.delete_entry(index[0])


class GoalDataframe(Dataframe):
    """
    Dataframe that contains the information about the goals the user set.
    """

    def __init__(self):
        super().__init__(column_names=[
            "value", "unit", "time_scale", "start_date", "end_date", "exercise"])

    def add_goal(self, new_entry: Goal):
        """
        Add a new goal as a new row to the dataframe.
        """
        self.data = pd.concat([self.data, pd.DataFrame({"value": [new_entry.value],
                                                        "unit": [new_entry.unit],
                                                        "time_scale": [new_entry.time_scale],
                                                        "start_date": [new_entry.start_date.print()],
                                                        "end_date": [new_entry.end_date.print()],
                                                        "exercise": [new_entry.exercise]})], ignore_index=True)
        # make sure duplicated entries are not possible
        if sum(self.data.duplicated()) > 0:
            print(
                "This goal is already present in the table, the second entry will be dropped.")
            self.data.drop_duplicates(inplace=True)


    def plot_goals(self):
        """
        Transform the data of the goal dataframe to use it for plotting
        """
        self.data['start_date'] = self.data['start_date'].apply(self.extract_date)
        self.data['end_date'] = self.data['end_date'].apply(self.extract_date)
        self.data['value'] = self.data['value'].apply(self.extract_float)
        self.data['time_scale'] = self.data['time_scale'].apply(self.extract_integer)

    def extract_integer(self,value:str):
        """
        Transform the time_scale string in a int for plotting the goals.
        """
        return int(value)
    
    def extract_float(self,value:str):
        """
        Transform the value string in a float for plotting the goals.
        """
        return float(value)
    
    def test_values(self):
        """
        Test that the dataframe doesn't contains unrealistic values
        """
        index = self.data.index[(self.data['value'] == 0) & (self.data['start_date'] == Date(1,1,1).print()) &
                                (self.data['end_date'] == Date(1,1,2).print())].to_list()
        print(index)
        if len(index) != 0:
            # drop all the lines with unrealist values
            self.delete_entry(index[0])


if __name__ == "__main__":
    my_workout_df = WorkoutDataframe()
    my_workout_df.print_dataframe()
    my_goals_df = GoalDataframe()
    my_goals_df.print_dataframe()

    # create a workout and a goal to store in the dataframe
    my_start_date = Date(2024, 5, 3)
    my_end_date = Date(2024, 10, 31)
    my_duration = Duration(hours=5)
    my_duration_goal = DurationGoal(value=my_duration, time_scale=7,
                                         start_date=my_start_date.print(),
                                         end_date=my_end_date.print())
    my_duration = Duration(minutes=90)
    my_calories = Calories(230, unit="kcal")
    my_workout = Climbing(my_calories, my_start_date, my_duration, 7)
    my_duration_goal = DurationGoal(value=my_duration, time_scale=7,
                                         start_date=my_start_date,
                                         end_date=my_end_date)

    # add the entries to the dataframe
    my_workout_df.add_workout(my_workout)
    my_workout_df.print_dataframe()
    my_goals_df.add_goal(my_duration_goal)
    my_goals_df.print_dataframe()

    # check some other functions of the Parent Class
    my_goals_df.add_goal(my_duration_goal)
    my_goals_df.edit_dataframe("value", 0, Duration(minutes=120))
    my_goals_df.print_dataframe()
