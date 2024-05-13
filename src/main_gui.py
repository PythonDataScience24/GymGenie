import tkinter as tk
import numpy as np
import os
import pandas as pd
import workout
import datetime
import dataframe
import gui
from calories import Calories
from date import Date
from distance import Distance
from duration import Duration
from date import Date
from rating import Rating

# Color palette for the GymGenie GUI.
black = "BLACK"
white = "WHITE"
dark_red = "#9B2226"
red = "#AE2012"
brown = "#BB3E03"
orange = "#CA6702"
yellow = "#EE9B00"
dark_blue = "#005F73"
blue = "#357F93"
light_blue = "#5d99a9"

def display_start_page():
    """
    Displays the startpage of the workout-application where the user can choose to log a workout,
    set a new goal, look at the overview of their goals or look at the trends in their workouts.
    """

    # Create root window
    global root
    root = tk.Tk()
    root.geometry("500x400")
    root.title("GymGenie")

    # Create frame for the main page
    main_frame = gui.create_frame(root=root, rows=6)

    # Add welcome label
    welcome_label = gui.create_label(frame=main_frame, text = "Welcome to GymGenie!", 
                                     font =("Arial", 16, "bold"), width=20)
    welcome_label.grid(column=0, row=0)

    # Initialize list of buttons containing the button-text and which command should be executed 
    # when the button is clicked.
    start_page_buttons = [("Log a workout", lambda: choose_workout(root)), 
                          ("Set a new goal", lambda: set_goal(root)),
                          ("View goals", lambda: view_goals(root)), 
                          ("View progress and trends", lambda: view_progress_and_trends(root)),
                          ("Quit", lambda: quit(root))]

    # Create and place the buttons on the main frame.
    for i, button in enumerate(start_page_buttons):
        start_page_button = gui.create_button(frame=main_frame, command=button[1],
                                              text=button[0], height=2)
        start_page_button.grid(column=0, row=i+1)

    tk.mainloop()

def choose_workout(root):
    """
    Displays the page where you can choose which type of workout to log after the
    "Log a workout"-button is clicked.

    Parameters
    ----------
    root : tkinter.Window
        The root window of the GUI for GymGenie.
    """
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Create frame where you can choose the type of workut you want to log your exercise for. 
    rows= len(workout.Workout.__subclasses__()) + 2 # include all workout types + label and exit-button
    choose_workout_frame = gui.create_frame(root=root, rows=rows)   

    # Add label that asks for the type of workout.
    label = gui.create_label(frame=choose_workout_frame, text = "What type of workout did you do?",
                             font =("Arial", 14, "bold"), width=40)
    label.grid(column=0, row=0)

    # Create list containing the names of all the workout types of class Workout.
    workout_types = [subclass.__name__ for subclass in workout.Workout.__subclasses__()]

    # Create a button for each workout type with a command that let's the user log the workout.
    # Thanks to stackoverflow there is a solution.Before it always had as workout class Other(last in the list)
    # because it call the function after the loop and for this was always the last values.
    # Since you are in a list I think you can just do for workout_type in workout_types, but I leave it to you if you
    # want to change or not.
    for i, workout_type in enumerate(workout_types):
        print(workout_type)
        choose_workout_button = gui.create_button(frame=choose_workout_frame, 
                                                  command=lambda workout_type=workout_type: log_workout(workout_type),
                                                  text=workout_type)
        choose_workout_button.grid(column=0, row=i+1)

    # Add exit button
    exit_button = gui.create_button(frame=choose_workout_frame, command=lambda: exit(root),
                                    text = "Exit", width=5)
    exit_button.grid(column=0, row=rows)

def log_workout(workout_type):
    """
    Diplays the page where you can log workput data for a specific type of workput.

    Parameters
    ----------
    root : tkinter.Window
        The root window of the GUI for GymGenie.

    workout_type : str
        The type of workout the user want to log. 
        Expected values are the subclasses of Workout: workout.Workout.__subclasses__().
    """
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Configure rows according to the number of datatypes that should be logged for the specific workout type
    if workout_type == "Climbing" or workout_type == "Strength":
        workout_datatypes = ["Calories", "Date ", "Duration", "Rating"]
    else:
        workout_datatypes = ["Calories", "Date", "Distance", "Duration", "Rating"]
    rows=len(workout_datatypes)+3 # include all datatypes + title, save-button and exit-button

    # Create frame where you can choose log in all the dta from your workout.    
    log_workout_frame = gui.create_frame(root=root, pady=10, columns=5, rows=rows)

    # Add top-label for the log workout-page
    log_workout_label = gui.create_label(frame=log_workout_frame, text="Log your workout:",
                                         font=("Arial", 16, "bold"))
    log_workout_label.grid(column=1, row=0, columnspan=3, sticky="ew")

    # Create widgets for entering the workout data.
    for i, workout_datatype in enumerate(workout_datatypes):
        # Create labels for each datatype that should be inputed and place them in the first column.
        datatype_label = gui.create_label(frame=log_workout_frame, text = f"{workout_datatype}:")
        datatype_label.grid(column=0, row=i+1, sticky="e")

        # Calories: insert an entry and a dropdown menu with options for the unit.
        if workout_datatype == "Calories":
            global calories_entry
            calories_entry = gui.create_entry(frame=log_workout_frame)
            calories_entry.grid(column=1, row=i+1)
            calories_units = ["kcal", "kJ"]

            global selected_unit_calories 
            selected_unit_calories = tk.StringVar(root)
            selected_unit_calories.set(calories_units[0])
            calories_units_options = gui.create_option_menu(frame=log_workout_frame, options=calories_units,
                                                            selected_option=selected_unit_calories) 
            calories_units_options.grid(column=2, row=i+1)       

        # Distance: insert an entry and a dropdown menu with options for the unit.
        if workout_datatype == "Distance":
            global distance_entry
            distance_entry = gui.create_entry(log_workout_frame)
            distance_entry.grid(column=1, row=i+1)

            global selected_unit_distance
            distance_units = ["km", "m", "miles"]
            selected_unit_distance = tk.StringVar(root)
            selected_unit_distance.set(distance_units[0])
            distance_units_options = gui.create_option_menu(frame=log_workout_frame, options=distance_units,
                                                       selected_option=selected_unit_distance) 
            distance_units_options.grid(column=2, row=i+1)

        # Rating: insert slider and label describing the scale
        if workout_datatype == "Rating":
            global rating_slider
            rating_slider = gui.create_scale(frame=log_workout_frame)
            rating_slider.grid(column=1, row=i+1)
            rating_label = gui.create_label(frame=log_workout_frame, text="Rate workout: 1=Easy, 10=Hard")
            rating_label.grid(column=2, row=i+1, columnspan=2, sticky="ew")


        # Duration: insert an entry and a label specifying the unit (min)
        if workout_datatype == "Duration":
            global hours_entry
            hours_entry = gui.create_entry(log_workout_frame)
            hours_entry.grid(column=1, row=i+1)
            hours_label = gui.create_label(frame=log_workout_frame, text="hours")
            hours_label.grid(column=2, row=i+1, sticky="w")

            global minutes_entry
            minutes_entry = gui.create_entry(log_workout_frame)
            minutes_entry.grid(column=3, row=i+1)
            minutes_label = gui.create_label(frame=log_workout_frame, text="minutes")
            minutes_label.grid(column=4, row=i+1, sticky="w")
            

        # Date: insert a label with the date and a button that allows user to choose the date.
        if workout_datatype == "Date":
            global selected_date
            selected_date = tk.StringVar()
            selected_date.set(datetime.date.today()) # Set the date initial date to todays date.
            date_label = gui.create_label(frame=log_workout_frame, textvariable=selected_date)
            date_label.grid(column=1, row=i+1)
            calendar_button = gui.create_button(frame=log_workout_frame, 
                                                command= lambda: gui.open_calendar(root, selected_date),
                                                text="Select a date", font=("Arial", 10, "bold"), width=12)
            calendar_button.grid(column=2, row=i+1)
    
    # Add save-button(save all the logged data put in by the user)
    save_button = gui.create_button(frame=log_workout_frame, text="Save", width=10,
                                command=lambda: save_data(frame=log_workout_frame, 
                                                          workout_type=workout_type))
    save_button.grid(columns=5, row=len(workout_datatypes)+1)

    #Add exit button
    exit_button = gui.create_button(frame=log_workout_frame, command=lambda: exit(root),
                                    text = "Exit", width=5, font=("Arial", 10, "bold"))
    exit_button.grid(column=4, row=len(workout_datatypes)+2)

def save_data(frame, workout_type):
    """
    Saves the logged workout data on the log workout-page.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame containing the logged workout data.

    workout_type : str
        The type of workout being logged as a string.
    """

    # Create objects for each datatype the user has entered.
    calories = Calories(calories=calories_entry.get(), unit=selected_unit_calories.get())
    rating = Rating(rating=rating_slider.get())
    duration = Duration(hours=int(hours_entry.get()), minutes=int(minutes_entry.get()))
    date_tmp = selected_date.get().split('-')
    date = Date(int(date_tmp[0]), int(date_tmp[1]), int(date_tmp[2]))
    # globals is a dictionary. If you want to verify if contains a value you need to extract all values of the keys using values()
    if distance_entry in globals().values():
        distance_value = Distance(distance=distance_entry.get(), unit=selected_unit_distance.get())
    else:
        distance_value = Distance(distance=np.NaN,unit='km')

    # Create a workout object and store it in a dataframe format.
    print(type(workout_type))
    workout_type = getattr(workout, workout_type)
    print(workout_type)
    my_workout = workout_type(calories=calories.print(), rating=rating.print(), duration=duration.__str__(), date=date.print(), distance=distance_value.print())

    # Check if a workout dataframe already exists. If not, create one.
    current_directory = os.getcwd().replace(os.sep,'/')
    workout_file = current_directory + "/logWorkouts.csv"
    try:
        workouts_df_data = pd.read_csv(workout_file)
        workouts_df = dataframe.WorkoutDataframe()
        workouts_df.data = workouts_df_data
    except FileNotFoundError:
        workouts_df = dataframe.WorkoutDataframe()

    # Add the workout object to the dataframe and save as csv file
    workouts_df.add_workout(my_workout)

    # Save dataframe in a file csv
    workouts_df.save_dataframe("logWorkouts.csv")

    # Close root window and display start page again. 
    root.destroy()
    display_start_page()
         

def set_goal(root):
    """

    """
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Create frame for the page where the user can set goals
    set_goal_frame = tk.Frame(root, bg=blue, pady=40) # frame can be renamed so it fits best with your code.
    set_goal_frame.pack(fill=tk.BOTH, expand=True) 
    

def view_goals(root):
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Create frame for the page where the user can view the goals
    view_goal_frame = tk.Frame(root, bg=blue, pady=40) # same here for renaming
    view_goal_frame.pack(fill=tk.BOTH, expand=True)

def view_progress_and_trends(root):
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Create frame for the page where the user can view progress and trends of their workout.
    progress_trend_frame = tk.Frame(root, bg=blue, pady=40)
    progress_trend_frame.pack(fill=tk.BOTH, expand=True)

def quit(root):
    """
    Closes the window of the application.

    Parameters
    ----------
    root : tkinter.Window
        The root window of the GUI for GymGenie.
    """
    root.destroy()


def exit(root):
    """
    Closes the current frame and open the start page.

    Parameters
    ----------
    root : tkinter.Window
        The root window of the GUI for GymGenie.
    """
    root.destroy()

    display_start_page()

if __name__ == "__main__":
    display_start_page()