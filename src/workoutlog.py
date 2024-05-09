import numpy as np
import calories, date, distance, duration, rating, dataframe, workout

class Workoutlog:
    """
    This class collect the information of a workout of a user and save it in a workout data object
    Args:
    exercise_types: list of different types of exercises
    distance_exercises: list of exercises that requires a distance question
    """

    def __init__(self,exercise_types:list, distance_exercises:list):
        self.exercise_types = exercise_types
        self.distance_exercises = distance_exercises


    def workout(self):
        """
        This function ask the users multiple question related to the different object present in a workout object.
        """
        NUMBER = "Please enter a number."
        #enter the date of the workout, make it NA if the input was invalid (maybe better do some way of asking again?)
        try:
            exercise_date_list = input("Enter the date you did this workout [dd/mm/yyyy]: ").split("/")
            exercise_date = date.Date(year = int(exercise_date_list[2]), month = int(exercise_date_list[1]), day = int(exercise_date_list[0]))
        except ValueError:
            print("Please enter your date in the format dd/mm/yyyy.")
            exercise_date = date.Date(1,1,1)

        #choose the exercise type
        print(self.exercise_types)
        exercise_type = input("Enter the type of exercise you did. Choose from the list above.\n").lower()
        while exercise_type not in self.exercise_types:
            exercise_type = input("Enter the type of exercise you did. Choose from the list above.\n").lower()
        
        #enter exercise duration
        try:
            exercise_duration = duration.Duration(minutes = int(input("Enter the duration of the workout in minutes.\n")))
        except ValueError:
            print(NUMBER)
            exercise_duration = duration.Duration(0,0)


        #ask for distance if it is an exercise type where that is necessary
        if exercise_type in self.distance_exercises:
            try:
                distance_value = distance.Distance(input("Enter the distance you completed in your workout in km.\n"), "km")
            except ValueError:
                print(NUMBER)
                distance_value = distance.Distance(np.NaN, "km")
        else:
            distance_value = distance.Distance(np.NaN, "km")

        #enter the calories
        try:
            calories_used = calories.Calories(input("Enter how many calories you burned in your workout in kcal.\n"), "kcal")
        except ValueError:
            print(NUMBER)
            calories_used = calories.Calories(0, "kcal")

        #enter the impression
        try:
            impression = rating.Rating(int(input("How did your workout feel on a scale from 1 to 10 (1=easy, 10=super hard).\n")))
        except ValueError:
            print("Rating should be bewtween 1 and 10.")
            impression = rating.Rating(1)
        

        # refactor this part of the code in a better way
        # TODO
        "running", "cycling", "strength", "swimming", "hiking/walking", "skiing", "others"
        match exercise_type:
            case "running":
                exercise_name = workout.Running(calories=calories_used.print(), date=exercise_date.print(),distance=distance_value.print(),duration=exercise_duration.__str__(),rating=impression.print())
            case "cycling":
                exercise_name = workout.Cycling(calories_used.print(), exercise_date.print(),distance_value.print(),exercise_duration.__str__(),impression.print())
            case "strength":
                exercise_name = workout.Strength(calories_used.print(),exercise_date.print(),exercise_duration.__str__(),impression.print())
            case "swimming":
                exercise_name = workout.Swimming(calories_used.print(), exercise_date.print(),distance_value.print(),exercise_duration.__str__(),impression.print())
            case "walking":
                exercise_name = workout.Walking(calories_used.print(), exercise_date.print(),distance_value.print(),exercise_duration.__str__(),impression.print())
            case "skiing":
                exercise_name = workout.Skiing(calories_used.print(), exercise_date.print(),distance_value.print(),exercise_duration.__str__(),impression.print())
            case "climbing":
                exercise_name = workout.Climbing(calories_used.print(),exercise_date.print(),exercise_duration.__str__(),impression.print())
            case "others":
                exercise_name = workout.Other(calories_used.print(), exercise_date.print(),distance_value.print(),exercise_duration.__str__(),impression.print())


        new_workout = dataframe.WorkoutDataframe()
        new_workout.add_workout(exercise_name)
        print(new_workout.print_dataframe())
        confirm = input("This is your entry, do you want to save it [y/n]? ").lower().strip()

        return confirm, exercise_name