from calories import Calories
from date import Date
from distance import Distance
from duration import Duration
from rating import Rating
from dataframe import WorkoutDataframe
from workout import Running, Climbing, Cycling, Skiing, Strength, Swimming, Walking, Other


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
            except ValueError:
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
        if exercise_type in self.distance_exercises:
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
                ), distance_value.print(), exercise_duration.print, impression.print())
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
