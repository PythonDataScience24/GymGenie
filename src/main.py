import sys
from workoutlog import WorkoutLog, SetGoal
from goal_summary import GoalSummary, WorkoutSummary
import os
from dataframe import WorkoutDataframe, GoalDataframe

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

        workouts_df = WorkoutDataframe()
        try:
            workouts_df.read_from_csv(workout_file)
        except FileNotFoundError:
            pass

        # start a dataframe to store the goals and load them from a file
        goal_file = current_directory + "/GoalData.csv"
        goals_df = GoalDataframe()
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
                sys.exit("GymGenie has been terminated. See you next time!")
            case _:
                print("Please type a valid option (w,g,o,s,q).")


def logWorkout(workouts_df, exercise_types, distance_exercises):
    """
    Allows the user to enter a workout and add it to the dataframe of workouts.

    Args:
    workouts_df : pandas.DataFrame
        Dataframe containing entries of previously logged workouts.
    exercise_types : list
        List of possible types of exercises to choose for a workout.
    distance_exercises : list
        List of types of exercises where it is appropriate to enter a distance value.
    """
    confirm = ""

    while confirm != "y":
        workout_respond, new_workout = WorkoutLog(exercise_types=exercise_types, 
                        distance_exercises=distance_exercises).collect_workout_info()

        if workout_respond == "y":
            confirm = "y"
            workouts_df.add_workout(new_workout)
            print(workouts_df.print_dataframe())

            # save dataframe in a file csv
            workouts_df.save_dataframe("logWorkouts.csv")
        elif workout_respond == 'n':
            # modify dataframe
            new_entry = ""
            while new_entry != 'y':
                row_index,column_name,new_value = WorkoutLog(exercise_types, 
                                            distance_exercises).modify_workout_dataframe()
                workouts_df.edit_dataframe(column_name,row_index,new_value)
                print(workouts_df.print_dataframe())
                response = input(
                "This is your new entry, do you want to save it? [y/n]: ").lower().strip()
                if response == 'y':
                    new_entry = 'y'
            confirm = 'y'
        else:
            print('Please select a valid confirmation answer!')

def setGoal(goal_df, exercise_types):
    """
    Allows the user to enter a workout and add it to the dataframe of workouts.

    Args:
    goal_df : pandas.DataFrame
        Dataframe containing entries of previously set goals.
    exercise_types : list
        List of possible types of exercises to choose for a workout.
    """
    confirm = ""

    while confirm != "y":
        goal_respond, new_goal = SetGoal(exercise_types).collect_goal_infos()
        if goal_respond == "y":
            confirm = 'y'
            goal_df.add_goal(new_goal)
            goal_df.save_dataframe("GoalData.csv")
        elif goal_respond == 'n':
            # modify dataframe
            new_entry = ""
            while new_entry != 'y':
                row_index,column_name,new_value = SetGoal(exercise_types).modify_entry_dataframe()
                goal_df.edit_dataframe(column_name,row_index,new_value)
                print(goal_df.print_dataframe())
                response = input(
                "This is your new entry, do you want to save it? [y/n]: ").lower().strip()
                if response == 'y':
                    new_entry = 'y'
            confirm = 'y'
        else:
            print('Please select a valid confirmation answer!')



def seeGoals(workout_df: WorkoutDataframe, goals_df: GoalDataframe):
    """
    Allow the user to see the progress made towards the goal

    Args:
    workout_df:pandas.DataFrame
        Dataframe containing entries of previously logged workouts.
    goals_df:pandas.DataFrame
        Dataframe containing entries of previously set goals.
    """
    # transform the dataframe of workout and goals for plotting
    workout_df.plot_dataframe()
    goals_df.plot_goals()

    summary = GoalSummary(workout_df,goals_df)

    #print all the goals and ask the user to select the one they want to see the plots for
    goals_df.print_dataframe()
    row_index = int(input("For which goal would you like to see the progress plots? Enter the row index: "))
    if row_index in goals_df.data.index:
        # visualize the progress in the goal
        summary.plot_goal(row_index)
    else:
        print("Please insert a valid index.")
    


def summaryVisualisations(workout_df):
    """
    Allow the user to see a summary of the workouts made

    Args:
    workout_df: pandas.DataFrame
        Dataframe containing entries of previously logged workouts.
    """
    #exercises = ###how to get this input?
    workout_summary = WorkoutSummary(workout_df)
    # retrieve timescale and quantity
    timescale = workout_summary.get_timescale()
    quantity = workout_summary.get_quantity()
    # plot the summary of the workouts of the user
    workout_summary.plot_summary(timescale, quantity)
    # plot the distribution of rating pro exercise
    workout_summary.plot_rating_by_exercises()

if __name__== "__main__":
    main()
