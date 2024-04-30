import pandas as pd
import numpy as np
import sys
import Activity, calories, date, distance, Duration, WorkoutRating

class Workout:


    def __init__(self,exercise_types, distance_exercises):
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
        except ValueError:
            print("Please enter your date in the format dd/mm/yyyy/h/min.")
            exercise_date = np.NaN

        #choose the exercise type
        print(self.exercise_types)
        exercise_type = Activity.Exercise(input("Enter the type of exercise you did. Choose from the list above.\n").lower())#really not robust way to do the input, but easiest thing i came up with
        while exercise_type.print() not in self.exercise_types:
            exercise_type = Activity.Exercise(input("Enter the type of exercise you did. Choose from the list above.\n").lower())
        
        #enter exercise duration
        try:
            exercise_duration = Duration.duration(minutes = input("Enter the duration of the workout in minutes.\n"))
        except ValueError:
            print(NUMBER)
            exercise_duration = np.NaN


        #ask for distance if it is an exercise type where that is necessary
        if exercise_type.print() in self.distance_exercises:
            try:
                distance_value = distance.Distance(input("Enter the distance you completed in your workout in km.\n"), "km")
            except ValueError:
                print(NUMBER)
                distance_value = np.NaN
        else:
            distance_value = np.NaN

        #enter the calories
        try:
            calories_used = calories.Calories(input("Enter how many calories you burned in your workout in kcal.\n"), "kcal")
        except ValueError:
            print(NUMBER)
            calories_used = np.NaN

        #enter the impression
        impression = WorkoutRating.WorkoutRating(input("How did your workout feel on a scale from 1 to 10 (1=easy, 10=super hard).\n"))
        

        #create a dataframe of these entries, then add them to the workouts dataframe (no idea if that is a good way to do it memory/computation wise?)
        #putting the values in a list was necessary to make the pd.DataFrame function run without error
        new_workout = pd.DataFrame({"date":[exercise_date.print()], "exercise type":[exercise_type.print()], "duration":[exercise_duration.__str__()], "distance":[distance_value.print()], "calories":[calories_used.print()], "impression": [impression.print()]})

        print(new_workout) #I'm not sure if it will actually print the objects in the dataframe (even if we have __str__ functions for each class) or just this kind of thing <WorkoutRating.WorkoutRating object at 0x00000...
        confirm = input("This is your entry, do you want to save it [y/n] ? ").lower().strip()

        return confirm, new_workout