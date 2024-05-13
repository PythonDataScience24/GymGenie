import sys
from workoutlog import WorkoutLog, SetGoal
from goal_summary import GoalSummary, WorkoutSummary
import os
import dill as pickle
from dataframe import WorkoutDataframe, GoalDataframe

def main():
    #define list of possible workouts
    exercise_types = ["running", "cycling", "strength", "swimming", "walking", "skiing", "climbing", "others"]
    distance_exercises = ["running", "cycling", "swimming", "walking", "skiing", "others"]

    choice = ""

    while choice != "q":
        choice = input("Welcome to GymGenie!\n Press 'w' to log a workout\n Press 'g' to set a new goal\n Press 'o' to get an overview over your goals\n Press 's' to see some summary visualisations\n Press 'q' to quit\n User: ")
        
        # Think how to improve this part
        #load the workouts from a pickle file, or start a dataframe to store them in if no file was found
        current_directory = os.getcwd().replace(os.sep,'/')
        workout_file = current_directory + "/logWorkouts"
        try:
            with open(f"{workout_file}.pkl", "rb") as file:
                workouts_df = pickle.load(file)
        except FileNotFoundError:
            workouts_df = WorkoutDataframe()

        # start a dataframe to store the goals and load them from a file
        goal_file = current_directory + "/GoalData"
        try:
            with open(f"{goal_file}.pkl", "rb") as file:
                goals_df = pickle.load(file)
        except FileNotFoundError:
            goals_df = GoalDataframe()

        match choice.lower().strip():
            case "w":
                logWorkout(workouts_df, exercise_types, distance_exercises)
            case "g":
                setGoal(goals_df, exercise_types)
            case "o":
                seeGoals(workouts_df.data, goals_df.data)
            case "s":
                summaryVisualisations(workouts_df.data)
            case "q":
                #save the workouts and goal dataframe when quitting to a csv
                workouts_df.save_to_csv(workout_file)
                goals_df.save_to_csv(goal_file)
                #also save them to a pickle file, from where we can reload the object structure
                with open(f"{workout_file}.pkl", "wb") as file:
                    pickle.dump(workouts_df, file)
                with open(f"{goal_file}.pkl", "wb") as file:
                    pickle.dump(goals_df, file)
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
            workouts_df.print_dataframe()

            # save dataframe in a file csv
            workouts_df.save_dataframe("logWorkouts.csv")
        else:
            print('Please select a valid confirmation answer or modify the workout')

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
        else:
            print('Please select a valid confirmation answer or modify the goal')



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
    try:   
        row_index = int(input("For which goal would you like to see the progress plots? Enter the row index: "))
        if row_index in goals_df.data.index:
            # visualize the progress in the goal
            summary.plot_goal(row_index)
        else:
            print("Please insert a valid index.")
    except ValueError:
        print("Please insert a valid index.")
    


def summaryVisualisations(workout_df: WorkoutDataframe):
    """
    Allow the user to see a summary of the workouts made

    Args:
    workout_df: pandas.DataFrame
        Dataframe containing entries of previously logged workouts.
    """
    workout_df.plot_dataframe()
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
