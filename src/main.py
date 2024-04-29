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
    date = pd.to_datetime(input("Enter the date you did this workout."))
    print(exercise_types)
    exercise_type = Activity.Exercise(input("Enter the type of exercise you did. Choose from the list above.").lower())#really not robust way to do the input, but easiest thing i came up with
    duration = Duration.duration(minutes = int(input("Enter the duration of the workout in minutes.")))
    if exercise_type in distance_exercises:
        distance = distance.Distance(float(input("Enter the distance you completed in your workout in km.")), "km")
    else:
        distance = np.NaN
    calories_used = calories.Calories(int(input("Enter how many calories you burned in your workout in kcal.")), "kcal")
    impression = WorkoutRating.WorkoutRating(input("How did your workout feel on a scale from 1 to 10 (1=easy, 10=super hard)."))
    

    #create a dataframe of these entries, then add them to the workouts dataframe (no idea if that is a good way to do it memory/computation wise?)
    #putting the values in a list was necessary to make the pd.DataFrame function run without error
    new_workout = pd.DataFrame({"date":[date], "exercise type":[exercise_type], "duration":[duration], "distance":[distance], "calories":[calories_used], "impression": [impression]})

    print(new_workout)
    confirm = input("This is your entry, do you want to save it? [y/n]").lower()

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