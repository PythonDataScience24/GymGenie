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
        #load the workouts from a csv file, or start a dataframe to store them in if no file was found
        current_directory = os.getcwd().replace(os.sep,'/')
        workout_file = current_directory + "/logWorkouts.csv"

        workouts_df = dataframe.WorkoutDataframe()
        try:
            workouts_df.read_from_csv(workout_file)
        except FileNotFoundError:
            pass

        # start a dataframe to store the goals and load them from a file
        goal_file = current_directory + "/GoalData.csv"
        goals_df = dataframe.GoalDataframe()
        try:
            goals_df.read_from_csv(goal_file)
        except FileNotFoundError:
            pass
        
        match choice.lower().strip():
            case "w":
                logWorkout(workouts_df, exercise_types, distance_exercises)
            case "g":
                setGoal(goals_df, exercise_types)
            case "o":
                seeGoals(workouts_df,goals_df)
            case "s":
                summaryVisualisations(workouts_df)
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
        new_goal = goal.DurationGoal(value = value, time_scale = time_scale, start_date = date.Date(year = int(start_date[2]), month = int(start_date[1]), day = int(start_date[0])), end_date = date.Date(year = int(end_date[2]), month = int(end_date[1]), day = int(end_date[0])), exercise = exercise_type)
    
    elif goal_type == "b":
        new_goal = goal.DistanceGoal(value = value, time_scale = time_scale, start_date = date.Date(year = int(start_date[2]), month = int(start_date[1]), day = int(start_date[0])), end_date = date.Date(year = int(end_date[2]), month = int(end_date[1]), day = int(end_date[0])), exercise = exercise_type)
    
    elif goal_type == "c":
        new_goal = goal.CalorieGoal(value = value, time_scale = time_scale, start_date = date.Date(year = int(start_date[2]), month = int(start_date[1]), day = int(start_date[0])), end_date = date.Date(year = int(end_date[2]), month = int(end_date[1]), day = int(end_date[0])), exercise = exercise_type)

    print(new_goal)
    confirm = input("This is your entry, do you want to save it? [y/n]\n").strip().lower()

    if confirm == "y":
        goal_df.add_goal(new_goal)
        goal_df.save_dataframe("GoalData.csv")


def seeGoals(workout_df: dataframe.WorkoutDataframe, goals_df: dataframe.GoalDataframe):

    summary = goal_summary.GoalSummary(workout_df,goals_df)

    #print all the goals and ask the user to select the one they want to see the plots for
    goals_df.print_dataframe()
    row_index = int(input("For which goal would you like to see the progress plots? Enter the row index.\n"))

    # visualize the progress in the goal
    summary.plot_goal(row_index)


def summaryVisualisations(workout_df):
    timescale = int(input("Over how many of the past days would you like to see the summary?\n"))
    quantity = input("Would you like to see the summary for duration, distance or calories?\n").lower().strip()
    #exercises = ###how to get this input?
    workout_summary = goal_summary.WorkoutSummary(workout_df)
    workout_summary.plot_summary(timescale, quantity)
    #workout_summary.compare_exercises(timescale,quantity, )
    workout_summary.plot_rating_by_exercises()

if __name__== "__main__":
    main()