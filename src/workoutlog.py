from calories import Calories
from date import Date
from distance import Distance
from duration import Duration
from rating import Rating
from dataframe import WorkoutDataframe,GoalDataframe
from workout import Running, Climbing, Cycling, Skiing, Strength, Swimming, Walking, Other
from goal import CalorieGoal,DistanceGoal,DurationGoal


class WorkoutLog:
    """
    This class collects information about a workout and saves it in a workout data object.

    Args:
    exercise_types: List of different types of exercises
    distance_exercises: List of exercises that require a distance question
    """

    def __init__(self, exercise_types: list, distance_exercises: list):
        self.exercise_types = exercise_types
        self.distance_exercises = distance_exercises
        self.workout_data = WorkoutDataframe()

    def collect_workout_info(self):
        """
        Collects information about the workout from the user.
        """
        try:
            exercise_date = self.get_exercise_date()
            exercise_type = self.get_exercise_type()
            exercise_duration = self.get_exercise_duration()
            distance_value = self.get_distance_value(exercise_type)
            calories_used = self.get_calories_used()
            impression = self.get_impression()

            exercise = self.create_exercise(exercise_type, exercise_date, exercise_duration,
                                            distance_value, calories_used, impression)

            self.workout_data.add_workout(exercise)
            print(self.workout_data.print_dataframe())

            confirm = input(
                "Do you want to save this entry? [y/n]: ").lower().strip()
            return confirm, exercise
        except ValueError as e:
            print(f"Error: {e}")
            return False, None

    def get_exercise_date(self):
        """
        Prompts the user to enter the date of the workout.
        """
        while True:
            try:
                date_str = input(
                    "Enter the date you did this workout [dd/mm/yyyy]: ").split('/')
                exercise_date = Date(year=int(date_str[2]), month=int(
                    date_str[1]), day=int(date_str[0]))
                return exercise_date
            except (ValueError, IndexError) as err:
                print(err)
                print("Please enter the date in the format dd/mm/yyyy.")
                return Date(1, 1, 1)

    def get_exercise_type(self):
        """
        Prompts the user to enter the type of exercise.
        """
        while True:
            print(self.exercise_types)
            exercise_type = input(
                "Enter the type of exercise you did: ").lower()
            if exercise_type in self.exercise_types:
                return exercise_type
            else:
                print("Invalid exercise type. Choose from the list above.")

    def get_exercise_duration(self):
        """
        Prompts the user to enter the duration of the workout.
        """
        while True:
            try:
                duration = int(
                    input("Enter the duration of the workout in minutes: "))
                return Duration(minutes=duration)
            except ValueError:
                print("Please enter a valid number for duration.")
                return Duration(0, 0)

    def get_distance_value(self, exercise_type):
        """
        Prompts the user to enter the distance if the exercise type requires it.
        """
        if exercise_type in self.distance_exercises or exercise_type.lower() in self.distance_exercises:
            while True:
                try:
                    distance = float(
                        input("Enter the distance you completed in km: "))
                    return Distance(distance=distance, unit='km')
                except ValueError:
                    print("Please enter a valid number for distance.")
                    return Distance(0, "km")
        else:
            return None

    def get_calories_used(self):
        """
        Prompts the user to enter the calories burned during the workout.
        """
        while True:
            try:
                calories = float(
                    input("Enter how many calories you burned in kcal: "))
                return Calories(calories=calories, unit='kcal')
            except ValueError:
                print("Please enter a valid number for calories burned.")
                return Calories(0, "kcal")

    def get_impression(self):
        """
        Prompts the user to rate how the workout felt.
        """
        while True:
            try:
                rating = int(
                    input("How did your workout feel on a scale from 1 to 10: "))
                if 1 <= rating <= 10:
                    return Rating(rating=rating)
                else:
                    print("Rating should be between 1 and 10.")
            except ValueError:
                print("Please enter a valid number for rating.")
                Rating(1)

    def create_exercise(self, exercise_type, exercise_date, exercise_duration,
                        distance_value, calories_used, impression):
        """
        Creates an exercise object based on the provided information.
        """
        match exercise_type:
            case "running":
                exercise_name = Running(calories=calories_used.print(),
                                        date=exercise_date.print(), distance=distance_value.print(),
                                        duration=exercise_duration.print(), rating=impression.print())
            case "cycling":
                exercise_name = Cycling(calories_used.print(), exercise_date.print(
                ), distance_value.print(), exercise_duration.print(), impression.print())
            case "strength":
                exercise_name = Strength(calories_used.print(
                ), exercise_date.print(), exercise_duration.print(), impression.print())
            case "swimming":
                exercise_name = Swimming(calories_used.print(), exercise_date.print(
                ), distance_value.print(), exercise_duration.print(), impression.print())
            case "walking":
                exercise_name = Walking(calories_used.print(), exercise_date.print(
                ), distance_value.print(), exercise_duration.print(), impression.print())
            case "skiing":
                exercise_name = Skiing(calories_used.print(), exercise_date.print(
                ), distance_value.print(), exercise_duration.print(), impression.print())
            case "climbing":
                exercise_name = Climbing(calories_used.print(
                ), exercise_date.print(), exercise_duration.print(), impression.print())
            case "others":
                exercise_name = Other(calories_used.print(), exercise_date.print(
                ), distance_value.print(), exercise_duration.print(), impression.print())

        return exercise_name
    
    def modify_workout_dataframe(self):
        """
        Collect information about the workout to modify
        """
        row_index = self.get_row_index()

        column_name = self.get_column()

        new_value = self.get_new_value(column_name)
        
        return row_index,column_name,new_value.print()

    def get_row_index(self):
        """
        Prompt the user which row wants to select in the workout dataframe
        """
        while True:
                
                self.workout_data.print_dataframe()
                try:
                    row_index = int(input("Which value would you like to modify? Enter the row index: "))
                    return row_index
                except ValueError as e:
                    print(f"Error {e}")
    
    def get_column(self):
        """
        Prompt the user which column wants to modify in the workout dataframe
        """
        #
        self.workout_data.print_dataframe()
        while True:
            column_name = input("Please enter the column name that you want to modify: ")

            if column_name in ["activity", "date", "duration", "distance", "calories", "rating"]:
                return column_name
            else:
                print('Please select a valid column name!')

    def get_new_value(self, name):
        """
        Ask the user which new value wants to insert in the dataframe
        """
        self.workout_data.print_dataframe()
        match name:
            case 'activity':
                value = self.get_exercise_type()
            case 'date':
                value = self.get_exercise_date()
            case 'duration':
                value = self.get_exercise_duration()
            case 'distance':
                value = self.get_distance_value(self.workout_data.data['activity'].item())
            case 'calories':
                value = self.get_calories_used()
            case 'rating':
                value = self.get_impression()

        return value

    

class SetGoal:


    def __init__(self, exercise_types:list):
        self.goal_df = GoalDataframe()
        self.exercise_types = exercise_types


    def collect_goal_infos(self):
        """
        Collect information about the goal from the user
        """
        try:
            goal_type = self.get_goal_type()
            goal_value = self.get_value()
            goal_timeframe = self.get_time_scale()
            goal_start_date = self.get_start_goal()
            goal_end_date = self.get_end_goal()
            goal_exercise = self.get_exercise_type()

            goal = self.create_goal_object(goal_type, goal_value,goal_timeframe, goal_start_date, goal_end_date, goal_exercise.capitalize())

            self.goal_df.add_goal(goal)
            print(self.goal_df.print_dataframe())

            confirm = input(
                "This is your entry, do you want to save it? [y/n]: ").lower().strip()
            return confirm, goal

        except ValueError as e:
            print(f"Error: {e}")
            return False,None


    def get_goal_type(self):
        """
        Prompts the user to enter the type of the goal
        """
        while True:
            goal_type = input("Do you want to set a goal for duration (a), distance (b) or calories (c)? Press a or b or c: ").strip().lower()
            if goal_type in ['a', 'b', 'c']:
                return goal_type
            else:
                print("Invalid entry! Please choose between a, b or c")

    def get_value(self):
        """
        Prompts the user to enter the value of the goal
        """
        while True:
            try:
                value = float(input("Which value do you want to reach with your goal? Please enter it in km, min or kcal: "))
                return value
            except ValueError:
                print("Please enter a valid entry!")
                return 0

    def get_time_scale(self):
        """
        Prompts the user to enter the timeframe of the goal
        """
        while True:
            try:
                time_scale = int(input("Per which timescale do you want to set your goal? (7/30/365): "))
                if time_scale in [7,30,365]:
                    return time_scale
            except ValueError:
                print("Please enter a valid entry!")

    def get_start_goal(self):
        """
        Prompts the user to enter the start date of the goal
        """
        while True:
            try:
                start_date = input("At what date do you start working on that goal? (dd/mm/yyyy): ").split("/")
                start = Date(year=int(start_date[2]), month=int(start_date[1]), day=int(start_date[0]))
                return start
            except (ValueError,IndexError) as err:
                print(err)
                print("Please enter the date in the format dd/mm/yyyy.")
                return Date(1,1,1)

    def get_end_goal(self):
        """
        Prompts the user to enter the end date of the goal
        """
        while True:
            try:
                end_date = input("Until which date do you want to reach the goal? (dd/mm/yyyy): ").split("/")
                end = Date(year=int(end_date[2]), month=int(end_date[1]), day=int(end_date[0]))
                return end
            except (ValueError,IndexError) as err:
                print(err)
                print("Please enter the date in the format dd/mm/yyyy.")
                return Date(1,1,2)

    def get_exercise_type(self):
        """
        Prompts the user to enter the type of exercise.
        """
        while True:
            print(self.exercise_types)
            exercise_type = input(
                "In which exercise do you want to achieve the goal? Choose from the list above or type 'all' to include all types of exercises.\n").lower()
            if exercise_type in self.exercise_types:
                return exercise_type
            elif exercise_type == 'all':
                return exercise_type
            else:
                print("Invalid exercise type. Choose from the list above.")

    
    def create_goal_object(self, goal_type,value,time_scale,start_date, end_date, exercise):
        """
        Create a goal object based on the information inserted before
        Args:
        value: The numeric value that the user want to reach
        times_scale: The user can choose between 7/30/365 days
        start_date: The date of start of the goal
        end_date: The date that the user wants to reach the goal
        exercise: The type of exercise in which the goal is set. It can be a specific exercises or all exercises.
        """
        match goal_type:

            case 'a':
                new_goal = DurationGoal(value=value, time_scale=time_scale,start_date=start_date, end_date=end_date, exercise=exercise)
            case 'b':
                new_goal = DistanceGoal(value=value, time_scale=time_scale, start_date=start_date, end_date=end_date, exercise=exercise)
            case 'c':
                new_goal = CalorieGoal(value=value, time_scale=time_scale, start_date=start_date, end_date=end_date, exercise=exercise)


        return new_goal
    

    def modify_entry_dataframe(self):
        """
        Collect information about the goal value to modify
        """
        row_index = self.get_row_index()
        column_name = self.get_column()

        new_input = self.get_new_value(column_name)

        return row_index,column_name,new_input

        

    def get_row_index(self):
        """
        Prompt the user which row wants to select in the goal dataframe
        """
        while True:
                print(self.goal_df.print_dataframe())
                try:
                    row_index = int(input("Which goal would you like to modify? Enter the row index: "))
                    return row_index
                except ValueError as e:
                    print(f"Error {e}")
    
    def get_column(self):
        """
        Prompt the user which column wants to modify in the goal dataframe
        """
        while True:
            column_name = input("Please enter the column name that you want to modify: ")

            if column_name in ['value', 'unit', 'time_scale', 'start_date', 'end_date', 'exercise']:
                return column_name
            else:
                print('Please select a valid column name!')
    def get_unit(self, choice):
        """
        Allow the user to choose the new goal value
        """
        match choice:
            case 'a':
                return 'min'
            case 'b':
                return 'km'
            case 'c':
                return 'kcal'

    def get_new_value(self, name):
        """
        Ask the user which new value wants to insert in the dataframe
        """

        match name:
            case 'value':
                value = self.get_value()
            case 'unit':
                value = self.get_unit(self.get_goal_type())
            case 'time_scale':
                value = self.get_time_scale()
            case 'start_date':
                value = self.get_start_goal()
            case 'end_date':
                value = self.get_end_goal()
            case 'exercise':
                value = self.get_exercise_type()

        return value



    





