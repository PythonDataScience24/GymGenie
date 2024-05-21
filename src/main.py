import sys
import utils as utl
import workout as wk
import goal_summary as gs
import workoutlog as wkl
import os

def main():
    #define list of possible workouts
    exercise_types = ["running", "cycling", "strength", "swimming", "walking", "skiing", "climbing", "others"]
    distance_exercises = ["running", "cycling", "swimming", "walking", "skiing", "others"]
    messages = ["You're on the right track, keep going!", "Consistency is key - keep going", "One step at a time, one day at a time - you're getting closer!"]

    choice = ""

    while choice != "q":
        choice = input("Welcome to GymGenie!\n Press 'w' to log a workout\n Press 'g' to set a new goal\n Press 'o' to get an overview over your goals\n Press 's' to see some summary visualisations\n Press 'q' to quit\n User: ")
        
        # Think how to improve this part
        #load the workouts from a pickle file, or start a dataframe to store them in if no file was found
        current_directory = os.getcwd().replace(os.sep,'/')
        workout_file = current_directory + "/logWorkouts.csv"
        workouts_df = utl.WorkoutDataframe()
        try:
            workouts_df.read_from_csv(workout_file)
        except FileNotFoundError:
            pass
        # start a dataframe to store the goals and load them from a file
        goal_file = current_directory + "/GoalData.csv"
        goals_df = utl.GoalDataframe()
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
                seeGoals(workouts_df, goals_df, messages)
            case "s":
                summaryVisualisations(workouts_df)
            case "q":
                #save the workouts and goal dataframe when quitting to a csv
                workouts_df.print_dataframe()
                goals_df.print_dataframe()
                workouts_df.save_to_csv(workout_file)
                goals_df.save_to_csv(goal_file)
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
        workout_respond, new_workout = wkl.WorkoutLog(exercise_types=exercise_types, 
                        distance_exercises=distance_exercises).collect_workout_info()

        if workout_respond == "y":
            confirm = "y"
            workouts_df.add_workout(new_workout)
            #workouts_df.print_dataframe()
            # test dataframe
            # checks that it doesn't contains any unrealistic values
            workouts_df.test_values()
            workouts_df.print_dataframe()
            # save dataframe in a file csv
            workouts_df.save_to_csv("logWorkouts.csv")
        elif workout_respond == "n":
            confirm = "y"
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
        goal_respond, new_goal = wkl.SetGoal(exercise_types).collect_goal_infos()
        if goal_respond == "y":
            confirm = "y"
            goal_df.add_goal(new_goal)
            #goal_df.print_dataframe()
            # checks for unrealistic values
            goal_df.test_values()
            goal_df.print_dataframe()
            goal_df.save_to_csv("GoalData.csv")
        elif goal_respond == "n":
            confirm = "y"
        else:
            print('Please select a valid confirmation answer or modify the goal')



def seeGoals(workout_df: utl.WorkoutDataframe, goals_df: utl.GoalDataframe, messages: list):
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

    summary = gs.GoalSummary(workout_df, goals_df, messages)

    #print all the goals and ask the user to select the one they want to see the plots for
    goals_df.print_dataframe()
    try:   
        row_index = int(input("For which goal would you like to see the progress plots? Enter the row index: "))
        if row_index in goals_df.data.index:
            # visualize the progress in the goal
            summary.plot_goal_terminale(row_index)
        else:
            print("Please insert a valid index.")
    except ValueError:
        print("Please insert a valid index.")
    


def summaryVisualisations(workout_df: utl.WorkoutDataframe):
    """
    Allow the user to see a summary of the workouts made

    Args:
    workout_df: pandas.DataFrame
        Dataframe containing entries of previously logged workouts.
    """
    workout_df.plot_dataframe()
    workout_summary = gs.WorkoutSummary(workout_df)
    # retrieve timescale, quantity and exercises
    timescale = workout_summary.get_timescale()
    quantity = workout_summary.get_quantity()
    exercises = workout_summary.get_exercises()
    # plot the summary of the workouts of the user
    workout_summary.plot_summary(timescale, quantity)
    #plot the comparison of the workouts of the user
    workout_summary.compare_exercises(timescale, quantity, exercises)
    # plot the distribution of rating pro exercise
    workout_summary.plot_rating_by_exercises()
    # plot pie
    workout_summary.plot_pie_sport(timescale,quantity)
    # plot scatter
    workout_summary.scatter_calories_duration()
    # calories / kilometer
    workout_summary.calories_per_distance()
    # calories / minutes
    workout_summary.calories_per_duration()

if __name__== "__main__":
    main()