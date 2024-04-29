import pandas as pd
import numpy as np
import sys
import Activity, calories, date, distance, Duration, workout_dataframe, Workout, WorkoutRating

def main():
    #start a dataframe to store the workouts in (later load this from a file)
    workouts_df = pd.DataFrame(columns=["date", "exercise type", "duration", "distance", "calories", "impression"])

    #define list of possible workouts
    exercise_types = ["running", "cycling", "strength", "swimming", "hiking/walking", "skiing", "others"]
    distance_exercises = ["running", "cycling", "swimming", "hiking/walking"]

    choice = ""

    while choice != "q":
        choice = input("Welcome to GymGenie! Press 'w' to log a workout, 'g' to set a new goal, 'o' to get an overview over your goals, 's' to see some summary visualisations or 'q' to quit.\n")

        match choice.lower().strip():
            case "w":
                logWorkout(workouts_df, exercise_types, distance_exercises)
            case "g":
                setGoal()
            case "o":
                seeGoals()
            case "s":
                summaryVisualisations()
            case "q":
                sys.exit("GymGenie has been terminated.")
            case _:
                print("Please type a valid option (w,g,o,s,q).")


def logWorkout(workouts_df, exercise_types, distance_exercises):
    """
    Allows the user to enter a workout and add it to the dataframe of workouts.

    Parameters
    ----------
    workouts_df : pandas.DataFrame
        Dataframe containing entries of previously logged workouts.
    exercise_types : list
        List of possible types of exercises to choose for a workout.
    distance_exercises : list
        List of types of exercises where it is appropriate to enter a distance value.
    """
    #enter the date of the workout, make it NA if the input was invalid (maybe better do some way of asking again?)
    try:
        exercise_date = input("Enter the date you did this workout.\n").split("/")
        exercise_date = date.Date(year = exercise_date[2], month = exercise_date[1], day = exercise_date[0])
    except:
        print("Please enter your date in the format dd/mm/yyyy.")
        exercise_date = np.NaN

    #choose the exercise type
    print(exercise_types)
    exercise_type = Activity.Exercise(input("Enter the type of exercise you did. Choose from the list above.\n").lower())#really not robust way to do the input, but easiest thing i came up with

    #enter exercise duration
    try:
        exercise_duration = Duration.duration(minutes = float(input("Enter the duration of the workout in minutes.\n")))
    except:
        print("Please enter a number.")
        exercise_duration = np.NaN


    #ask for distance if it is an exercise type where that is necessary
    if exercise_type in distance_exercises:
        try:
            distance = distance.Distance(float(input("Enter the distance you completed in your workout in km.\n")), "km")
        except:
            print("Please enter a number.")
            distance = np.NaN
    else:
        distance = np.NaN

    #enter the calories
    try:
        calories_used = calories.Calories(float(input("Enter how many calories you burned in your workout in kcal.\n")), "kcal")
    except:
        print("Please enter a number.")
        calories_used = np.NaN

    #enter the impression
    impression = WorkoutRating.WorkoutRating(input("How did your workout feel on a scale from 1 to 10 (1=easy, 10=super hard).\n"))
    

    #create a dataframe of these entries, then add them to the workouts dataframe (no idea if that is a good way to do it memory/computation wise?)
    #putting the values in a list was necessary to make the pd.DataFrame function run without error
    new_workout = pd.DataFrame({"date":[exercise_date], "exercise type":[exercise_type], "duration":[exercise_duration], "distance":[distance], "calories":[calories_used], "impression": [impression]})

    print(new_workout) #I'm not sure if it will actually print the objects in the dataframe (even if we have __str__ functions for each class) or just this kind of thing <WorkoutRating.WorkoutRating object at 0x00000...
    confirm = input("This is your entry, do you want to save it? [y/n]").lower().strip()

    if confirm == "y":
        workouts_df = pd.concat([workouts_df, new_workout])
    else:
        pass #not sure what to do in the else case, right now I just go back to the very start



def setGoal():
    pass

def seeGoals():
    pass

def summaryVisualisations():
    pass

if __name__== "__main__":
    main()