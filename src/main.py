import pandas as pd
import numpy as np

def main():
    #start a dataframe to store the workouts in (later load this from a file)
    workouts_df = pd.DataFrame(columns=["date", "exercise type", "duration", "distance", "calories", "impression"])

    #define list of possible workouts
    exercise_types = ["running", "cycling", "strength", "swimming", "hiking/walking", "skiing", "others"]
    distance_exercises = ["running", "cycling", "swimming", "hiking/walking"]

    choice = ""

    while choice != "q":
        choice = input("Welcome to GymGenie! Press 'w' to log a workout, 'g' to set a new goal, 'o' to get an overview over your goals, 's' to see some summary visualisations or 'q' to quit.")

        match choice.lower():
            case "w":
                logWorkout(workouts_df, exercise_types, distance_exercises)
            case "g":
                setGoal()
            case "o":
                seeGoals()
            case "s":
                summaryVisualisations()


def logWorkout(workouts_df, exercise_types, distance_exercises):
    date = pd.to_datetime(input("Enter the date you did this workout."))
    print(exercise_types)
    exercise_type = input("Enter the type of exercise you did. Choose from the list above.").lower() #really not robust way to do the input, but easiest thing i came up with
    duration = int(input("Enter the duration of the workout in minutes."))
    if exercise_type in distance_exercises:
        distance = int(input("Enter the distance you completed in your workout in km."))
    else:
        distance = np.NaN
    calories = int(input("Enter how many calories you burned in your workout in kcal."))
    impression = int(input("How did your workout feel on a scale from 1 to 10 (1=easy, 10=super hard)."))
    

    #create a dataframe of these entries, then add them to the workouts dataframe (no idea if that is a good way to do it memory/computation wise?)
    #putting the values in a list was necessary to make the pd.DataFrame function run without error
    new_workout = pd.DataFrame({"date":[date], "exercise type":[exercise_type], "duration":[duration], "distance":[distance], "calories":[calories], "impression": [impression]})

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

main()