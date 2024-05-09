import pandas as pd
import sys
import workoutlog, goal_summary, date
import os
import dataframe
import goal
import duration
import distance
import calories

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
            workouts_df_data = pd.read_csv(workout_file)
            #make it a WorkoutDataframe object
            workouts_df = dataframe.WorkoutDataframe()
            workouts_df.data = workouts_df_data
        except FileNotFoundError:
            workouts_df = dataframe.WorkoutDataframe()
        # start a dataframe to store the goals
        goal_file = current_directory + "/GoalData.csv"
        try:
            goals_df_data = pd.read_csv(goal_file)
            #make it a GoalDataframe object
            goals_df = dataframe.GoalDataframeDataframe()
            goals_df.data = goals_df_data
        except FileNotFoundError:
            goals_df = dataframe.GoalDataframe()
        
        match choice.lower().strip():
            case "w":
                logWorkout(workouts_df, exercise_types, distance_exercises)
            case "g":
                setGoal(goals_df, exercise_types)
            case "o":
                seeGoals(workouts_df,goals_df,exercise_types)
            case "s":
                summaryVisualisations()
            case "q":
                #save the workouts and goal dataframe when quitting
                workouts_df.save_dataframe(path = workout_file)
                goals_df.save_dataframe(path = goal_file)
                # exit the program
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
            workouts_df.add_workout(new_workout)
            print(workouts_df.print_dataframe())

            # save dataframe in a file csv
            workouts_df.save_dataframe("logWorkouts.csv")

def setGoal(goal_df, exercise_types):
    """
    Allows the user to enter a workout and add it to the dataframe of workouts.

    Parameters
    ----------
    goal_df : pandas.DataFrame
        Dataframe containing entries of previously set goals.
    exercise_types : list
        List of possible types of exercises to choose for a workout.
    """
    
    #ask for all the relevant user input
    goal_type = input("Do you want to set a goal for duration (a), distance (b) or calories (c)?\n").strip().lower()
    value = float(input("Which value do you want to reach with your goal? Please enter it in km, min or kcal.\n"))
    time_scale = int(input("Per which timescale do you want to set your goal? Please enter the days.\n"))
    start_date = input("At what date do you start working on that goal? (dd/mm/yyyy)\n").split("/")
    end_date = input("Until which date do you want to reach the goal? (dd/mm/yyyy)\n").split("/")
    print(exercise_types)
    exercise_type = input("In which exercise do you want to achieve the goal? Choose from the list above or type 'all' to include all types of exercises.\n")
        
    #create a Goal object from the input
    if goal_type == "a":
        new_goal = goal.DurationGoal(value = duration.Duration(minutes = value), time_scale = time_scale, start_date = date.Date(year = int(start_date[2]), month = int(start_date[1]), day = int(start_date[0])), end_date = date.Date(year = int(end_date[2]), month = int(end_date[1]), day = int(end_date[0])), exercise = exercise_type)
    
    elif goal_type == "b":
        new_goal = goal.DistanceGoal(value = distance.Distance(distance = value, unit = "km"), time_scale = time_scale, start_date = date.Date(year = int(start_date[2]), month = int(start_date[1]), day = int(start_date[0])), end_date = date.Date(year = int(end_date[2]), month = int(end_date[1]), day = int(end_date[0])), exercise = exercise_type)
    
    elif goal_type == "c":
        new_goal = goal.CalorieGoal(value = calories.Calories(calories = value, unit = "kcal"), time_scale = time_scale, start_date = date.Date(year = int(start_date[2]), month = int(start_date[1]), day = int(start_date[0])), end_date = date.Date(year = int(end_date[2]), month = int(end_date[1]), day = int(end_date[0])), exercise = exercise_type)

    print(new_goal)
    confirm = input("This is your entry, do you want to save it? [y/n]\n").strip().lower()

    if confirm == "y":
        goal_df.add_goal(new_goal)


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
