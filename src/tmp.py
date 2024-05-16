import numpy as np
from calories import Calories
from date import Date
from distance import Distance
from duration import Duration
from rating import Rating
from dataframe import WorkoutDataframe
from workout import Running,Climbing,Cycling,Skiing,Strength,Swimming,Walking,Other

# For the moment to keep later we can delete it -- DUPLICATE ---

class Workoutlog:
    """
    This class collect the information of a workout of a user and save it in a workout data object
    Args:
    exercise_types: list of different types of exercises
    distance_exercises: list of exercises that requires a distance question
    """

    def __init__(self, exercise_types: list, distance_exercises: list):
        self.exercise_types = exercise_types
        self.distance_exercises = distance_exercises

    def workout(self):
        """
        This function ask the users multiple question related to the different object 
        present in a workout object.
        """
        NUMBER = "Please enter a number."
        try:
            exercise_date_list = input(
                "Enter the date you did this workout [dd/mm/yyyy]: ").split("/")
            exercise_date = Date(year=int(exercise_date_list[2]), month=int(
                exercise_date_list[1]), day=int(exercise_date_list[0]))
        except ValueError:
            print("Please enter your date in the format dd/mm/yyyy.")
            exercise_date = Date(1, 1, 1)

        # choose the exercise type
        print(self.exercise_types)
        exercise_type = input(
            "Enter the type of exercise you did. Choose from the list above.\n").lower()
        while exercise_type not in self.exercise_types:
            exercise_type = input(
                "Enter the type of exercise you did. Choose from the list above.\n").lower()

        # enter exercise duration
        try:
            exercise_duration = Duration(minutes=int(
                input("Enter the duration of the workout in minutes.\n")))
        except ValueError:
            print(NUMBER)
            exercise_duration = Duration(0, 0)

        # ask for distance if it is an exercise type where that is necessary
        if exercise_type in self.distance_exercises:
            try:
                distance_value = Distance(
                    input("Enter the distance you completed in your workout in km.\n"), "km")
            except ValueError:
                print(NUMBER)
                distance_value = Distance(np.NaN, "km")
        else:
            distance_value = Distance(np.NaN, "km")

        # enter the calories
        try:
            calories_used = Calories(
                input("Enter how many calories you burned in your workout in kcal.\n"), "kcal")
        except ValueError:
            print(NUMBER)
            calories_used = Calories(0, "kcal")

        # enter the impression
        try:
            impression = Rating(int(input(
                "How did your workout feel on a scale from 1 to 10 (1=easy, 10=super hard).\n")))
        except ValueError:
            print("Rating should be bewtween 1 and 10.")
            impression = Rating(1)

        # refactor this part of the code in a better way
        # TODO
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

        new_workout = WorkoutDataframe()
        new_workout.add_workout(exercise_name)
        print(new_workout.print_dataframe())
        confirm = input(
            "This is your entry, do you want to save it [y/n]? ").lower().strip()

        return confirm, exercise_name