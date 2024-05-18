"""
This module collect all the object used in the implementation of the program
"""
from datetime import date
import numpy as np
from abc import ABC
import pandas as pd
import workout as wk
import workoutlog as wkl


class Date:
    """
    Represents the date and time in which the exercise was completed.

    Attributes:
        date_time (datetime.date) : the date when the exercise was completed.
    """
    def __init__(self, year: int, month: int, day: int) :
        self.date_time = date(year=year, month=month, day=day)
    

    def print(self):
        return self.date_time



class Distance:
    """
    Represents the distance completed in the exercise.

    Attributes:
        distance (float): The numeric value of the distance.
        unit (str): The unit of measurement ('km', 'm' or 'miles')

    """

    def __init__(self, distance: float, unit: str):
        """
        Initialize a Distance object

        Args:
            distance (float): The numeric value of the distance.
            unit (str): The unit of measurement ('km', 'm' or 'miles')
        """
        self.distance_value = distance
        self.unit = unit.lower()

    def distance_unit_setting(self, unit):
        """
        Set the distance unit.

        Args:
            unit (str): The desired unit ('km', 'm', or 'miles').
        """
        # Validate the unit
        valid_units = ['km', 'm', 'miles']
        if unit.lower() in valid_units:
            self.unit = unit.lower()
        else:
            raise ValueError(f"Invalid unit. Choose from {', '.join(valid_units)}.")

    def distance_convert(self, a, b):
        """
        Convert distance from one unit to another one.

        Args:
            distance (float) : The numeric value of the distance.
            a : current unit.
            b : desired unit to convert to .

        """
        # I am not sure if i should directly modify self.distance
        if a == 'km' and b == 'm':
            self.distance_value = self.distance_value*1000
        elif a == 'm' and b == 'km':
            self.distance_value = self.distance_value/1000
        elif a == 'miles' and b == 'km':
            self.distance_value = self.distance_value*1.60934
        elif a == 'km' and b == 'miles':
            self.distance_value = self.distance_value/1.60934
        elif a == 'm' and b == 'miles':
            self.distance_value = self.distance_value/1609.34
        elif a == 'miles' and b == 'm':
            self.distance_value = self.distance_value*1609.34

        # Round the distance value with 3 decimals
        self.distance_value = round(self.distance_value, 3)
        # Update the unit
        self.unit = b

    def print(self):

        if self.distance_value == np.NAN:
            return np.NAN
        else:
            return f"{self.distance_value} {self.unit}"

    def print_distance(self):
        if self.distance_value == np.NaN:
            return np.NaN
        else:
            return self.distance_value

class Duration:
    """
    Represents the duration of a workout.

    Attributes:
        hours (float): How many hours the workout lasted for.
        min (float): How many minutes the workout lasted for.
    """

    def __init__(self, hours=0, minutes=0):
        # Save duration as the total minutes spent.
        self.minutes = minutes + 60*hours

    def print(self):
        return self.short_str()

    def short_str(self):
        """
        Return duration in short string format. Example: "1h30".
        """
        return f"{self.get_hours()}h{self.get_minutes()}"

    def long_str(self):
        """
        Return duration in long string format. Example: "1 hours, 30 minutes".
        """
        return f"{self.get_hours()} hours, {self.get_minutes()} minutes"

    def get_hours(self):
        """
        Get the number of full hours of the duration.
        """
        return self.minutes // 60

    def get_minutes(self):
        """
        Get the number of residual minutes of the duration after the hours has been accounted for.
        """
        return self.minutes % 60

class Calories:
    """
    Represents the calories burnt during the exercise.
    
    Atributtes:
        calories (float) : Numeric value
        unit (str) : The unit of measurement ('kcal', 'kJ')
    """
    def __init__(self, calories:int, unit:str) :
        self.calories_value = calories
        self.unit = unit

    def __str__(self):
        return f"{self.calories_value} {self.unit}"

    # I am not sure if this function is useful at all
    def calories_unit_setting(self, unit):
        """
        Set the calories unit.

        Args:
            unit (str): The desired unit ('kcal' or 'kJ').
        """
        #Validate the unit
        valid_units = [ 'kcal', 'kJ']
        if unit in valid_units:
            self.unit = unit
        else:
            raise ValueError(f"Invalid unit. Choose from {', '.join(valid_units)}.")

    def calories_convert(self, a, b):
        """
        Convert calories from one unit to another one.

        Args:
            calories (float) : The numeric value of calories.
            a : current unit.
            b : desired unit to convert to .
        
        """
        #I am not sure if i should directly modify self.distance
        if a == 'kcal' and b == 'kJ':
            self.calories_value = self.calories_value*4.184
            self.unit = 'kJ'
        elif a == 'kJ' and b == 'kcal':
            self.calories_value = self.calories_value/4.184
            self.unit = 'kcal'

        
        #Round the distance value with 3 decimals 
        self.calories_value = round(self.calories_value, 3)
        # Update the unit
        self.unit = b
    def print(self):
        return f"{self.calories_value} {self.unit}"


class Rating:
    """
    A rating of how a workout felt like.

    Attributes:
        rating (int) : Rating of the workout (from 1 to 10)
    """
    def __init__(self, rating:int):
        self.rating_value = rating
    
    def print(self):
        return self.rating_value
class Goal:
    """
    Abstract base class for a goal.

    Attributes:
        value: actual value that should be reached with this goal
        unit: unit of the value the goal is set for
        time_scale: number of days over which you want to achieve your goal (e.g. 7 to set a goal of doing a certain amount each week)
        start_date (Date): date at which the goal was set
        end_date (Date): date by which the goal should be reached
        exercise (Workout): type of workout in which you want to achieve the goal. Default is 'All', to include all types of exercises.
    """

    def __init__(self, value: float, unit: str, time_scale: int, start_date: Date, end_date: Date, exercise='All'):
        if start_date.print() >= end_date.print():
            raise ValueError("The start_date must be before the end_date.")
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
        return f"Goal: {self.value} {self.unit} per {self.time_scale} days in exercise {self.exercise} \n Set on {self.start_date.print()}, to reach until {self.end_date.print()}"

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def subclass_name(self):
        """
        Returns the name of the subclass (quantity for which the goal is set, i.e. calories, duration or distance).
        """
        return self.__class__.__name__


class CalorieGoal(Goal):
    """
    A goal set for calories. See Goal for attributes. The attribute value has to be of class Calories.
    """

    def __init__(self, value, time_scale, start_date, end_date, exercise='All'):
        super().__init__(value, "kcal", time_scale, start_date, end_date, exercise)


class DistanceGoal(Goal):
    """
    A goal set for distances. See Goal for attributes. The attribute value has to be of class Distance.
    """

    def __init__(self, value, time_scale, start_date, end_date, exercise='All'):
        super().__init__(value, "km", time_scale, start_date, end_date, exercise)


class DurationGoal(Goal):
    """
    A goal set for duration of workouts. See Goal for attributes. The attribute value has to be of class Duration.
    """

    def __init__(self, value, time_scale, start_date, end_date, exercise='All'):
        super().__init__(value, "min", time_scale, start_date, end_date, exercise)


    
"""
This module contains the Class Dataframe and subclasses for dataframes to store Workouts or Goals with specific column names. The data is stored in the data attribute. Methods allow to save the dataframe, print it, edit or delete entries, and add new entries (rows).
"""
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

    def add_workout(self, new_entry: wk.Workout):
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
