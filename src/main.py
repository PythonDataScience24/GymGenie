import pandas as pd
import sys
import workoutlog, goal_summary, date
import os

def main():
    #define list of possible workouts
    exercise_types = ["running", "cycling", "strength", "swimming", "walking", "skiing", "climbing", "others"]
    distance_exercises = ["running", "cycling", "swimming", "walking"]

    choice = ""

    while choice != "q":
        choice = input("Welcome to GymGenie!\n Press 'w' to log a workout\n Press 'g' to set a new goal\n Press 'o' to get an overview over your goals\n Press 's' to see some summary visualisations\n Press 'q' to quit\n User: ")
        
        # Think how to improve this part
        #start a dataframe to store the workouts in (later load this from a file)
        current_directory = os.getcwd().replace(os.sep,'/')
        workout_file = current_directory + "/logWorkouts.csv"
        try:
            workouts_df = pd.read_csv(workout_file)
        except FileNotFoundError:
            workouts_df = pd.DataFrame(columns=['activity', 'date', 'duration','distance (km)' , 'calories (kcal)', 'rating'])
        # start a dataframe to store the goals
        goal_file = current_directory + "/GoalData.csv"
        try:
            goals_df = pd.read_csv(goal_file)
        except FileNotFoundError:
            goals_df = pd.DataFrame(columns=["value", "unit", "time_scale", "start_date", "end_date", "exercise"])
        #print(workouts_df)
        match choice.lower().strip():
            case "w":
                logWorkout(workouts_df, exercise_types, distance_exercises)
            case "g":
                setGoal()
            case "o":
                seeGoals(workouts_df,goals_df,exercise_types)
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

            #make sure duplicate entries are not possible
            if sum(workouts_df.duplicated()) > 0:
                print("This workout is already present in the table, the second entry will be dropped.")
                workouts_df.drop_duplicates(inplace = True)

            # save dataframe in a file csv
            workouts_df.to_csv("logWorkouts.csv", encoding='utf-8', index=False)

    
   




def setGoal():
    pass

def seeGoals(workout_df,goals_df, exercise_types):

    summary = goal_summary.GoalSummary(workout_df,goals_df)

    # ask for: 
    # time frame
    try:
        timeframe = input(int("How long was your goal in days? "))
    except ValueError:
        print("You need to insert a numer between 7/30/365!")
        timeframe =  None
    # start Date
    try:
        startDate = input("When did your goal started? [dd/mm/yyyy] ").split("/")
    except ValueError:
        print("Please enter your date in the format dd/mm/yyyy.")
        startDate = date.Date(1,1,1)
    # end Date
    try:
        endDate = input("When did your goal end? [dd/mm/yyyy] ").split("/")
    except ValueError:
        print("Please enter your date in the format dd/mm/yyyy.")
        endDate = date.Date(1,1,1)
    # which sport between the list
    print(exercise_types)
    activity = input("Enter the type of exercise you did. Choose from the list above. ").lower()
    while activity not in exercise_types:
            print(exercise_types)
            activity = input("Enter the type of exercise you did. Choose from the list above. ").lower()

    # visualize the progress in the goal
    print(summary.plot_goal(timeframe,startDate,endDate,activity))


def summaryVisualisations():
    pass

if __name__== "__main__":
    main()