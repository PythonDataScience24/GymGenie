import pandas as pd
import numpy as np
import sys
import calories, date, distance, duration, rating, workout_dataframe, workout

class Workoutlog:


    def __init__(self,exercise_types:list, distance_exercises:list):
        self.exercise_types = exercise_types
        self.distance_exercises = distance_exercises


    def workout(self):
        NUMBER = "Please enter a number."
        #enter the date of the workout, make it NA if the input was invalid (maybe better do some way of asking again?)
        try:
            exercise_date_list = input("Enter the date you did this workout [dd/mm/yyyy/h/min]: ").split("/")
            
            if len(exercise_date_list) == 3:
                exercise_date = date.Date(year = int(exercise_date_list[2]), month = int(exercise_date_list[1]), day = int(exercise_date_list[0]), h=0, min=0)
            elif len(exercise_date_list) == 4:
                exercise_date = date.Date(year = int(exercise_date_list[2]), month = int(exercise_date_list[1]), day = int(exercise_date_list[0]), h=int(exercise_date_list[3]), min=0)
            elif len(exercise_date_list) == 5:
                exercise_date = date.Date(year = int(exercise_date_list[2]), month = int(exercise_date_list[1]), day = int(exercise_date_list[0]), h=int(exercise_date_list[3]), min=int(exercise_date_list[4]))
            elif len(exercise_date_list) < 3:
                exercise_date = date.Date(1,1,1,0,0)
        except ValueError:
            print("Please enter your date in the format dd/mm/yyyy/h/min.")
            exercise_date = date.Date(1,1,1,0,0)

        #choose the exercise type
        print(self.exercise_types)
        exercise_type = input("Enter the type of exercise you did. Choose from the list above.\n").lower()#really not robust way to do the input, but easiest thing i came up with
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
            impression = rating.Rating(np.NaN)
        

        #create a dataframe of these entries, then add them to the workouts dataframe (no idea if that is a good way to do it memory/computation wise?)
        #putting the values in a list was necessary to make the pd.DataFrame function run without error
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


        new_workout = workout_dataframe.Workout_dataframe(exercise=exercise_name,date=exercise_name.get_date(), duration=exercise_name.get_duration(), distance=exercise_name.get_distance(),calories=exercise_name.get_calories(),rating=exercise_name.get_rating())
        print(new_workout.read_dataframe())
        confirm = input("This is your entry, do you want to save it [y/n]? ").lower().strip()

        return confirm, new_workout