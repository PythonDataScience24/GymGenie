import pandas as pd
import sys
import workoutlog
import os

def main():
    #define list of possible workouts
    exercise_types = ["running", "cycling", "strength", "swimming", "walking", "skiing", "others"]
    distance_exercises = ["running", "cycling", "swimming", "walking"]

    choice = ""

    while choice != "q":
        choice = input("Welcome to GymGenie!\n Press 'w' to log a workout\n Press 'g' to set a new goal\n Press 'o' to get an overview over your goals\n Press 's' to see some summary visualisations\n Press 'q' to quit\n User: ")
        
        #start a dataframe to store the workouts in (later load this from a file)
        current_directory = os.getcwd().replace(os.sep,'/')
        file_name = current_directory.replace(os.sep,'/') + "/logWorkouts.csv"
        try:
            workouts_df = pd.read_csv(file_name)
        except FileNotFoundError:
            workouts_df = pd.DataFrame(columns=['activity', 'date', 'duration (min)','distance (km)' , 'calories (kcal)', 'rating'])
        #print(workouts_df)
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
        workout_respond, new_workout = workoutlog.Workoutlog(exercise_types=exercise_types, distance_exercises=distance_exercises).workout()

        if workout_respond == "y":
            confirm = "y"
            workouts_df = pd.concat([workouts_df, new_workout.create_dataframe()], ignore_index=True)
            print(workouts_df)
            # save dataframe in a file csv
            workouts_df.to_csv("logWorkouts.csv", encoding='utf-8', index=False)

    
   




def setGoal():
    pass

def seeGoals():
    pass

def summaryVisualisations():
    pass

if __name__== "__main__":
    main()