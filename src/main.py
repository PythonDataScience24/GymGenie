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
        choice = input("Welcome to GymGenie!\n Press 'w' to log a workout\n Press 'g' to set a new goal\n Press 'o' to get an overview over your goals\n Press 's' to see some summary visualisations\n Press 'q' to quit\n User: ")

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
    confirm = ""

    while confirm != "y":
        workout_respond, new_workout = Workout.Workout(exercise_types=exercise_types, distance_exercises=distance_exercises).workout()

        if workout_respond == "y":
            confirm = "y"
            workouts_df = pd.concat([workouts_df, new_workout])



def setGoal():
    pass

def seeGoals():
    pass

def summaryVisualisations():
    pass

if __name__== "__main__":
    main()