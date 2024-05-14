import tkinter as tk
import numpy as np
import os
import pandas as pd
import random
import workout
import tkcalendar
import datetime
import goal
import gui
from tkinter import messagebox
from calories import Calories
from date import Date
from distance import Distance
from duration import Duration
from date import Date
from rating import Rating
import dataframe
from dataframe import WorkoutDataframe


### Global variables
#Create boolean values to keep the workflow
global set_distance
set_distance = False
global set_duration
set_duration = False
global set_calories
set_calories = False

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
    main_frame = gui.create_frame(root=root, rows=7)

    # Add welcome label
    welcome_label = gui.create_label(frame=main_frame, text = "Welcome to GymGenie!", 
                                     font =("Arial", 16, "bold"), width=20)
    welcome_label.grid(column=0, row=0)

    # Add logo - currently not working
    #logo = tk.PhotoImage(file="gymgenie_logo.png")
    #label = tk.Label(root, image=logo)
    #label.grid(col=0, row=1)

    # Initialize list of buttons containing the button-text and which command should be executed 
    # when the button is clicked.
    start_page_buttons = [("Log a workout", lambda: choose_workout(root)), 
                          ("Set a new goal", lambda: display_set_goal(root)),
                          ("View goals", lambda: view_goals(root)), 
                          ("View progress and trends", lambda: view_progress_and_trends(root)),
                          ("Quit", lambda: quit(root))]

    # Create and place the buttons on the main frame.
    for i, button in enumerate(start_page_buttons):
        start_page_button = gui.create_button(frame=main_frame, command=button[1],
                                              text=button[0], height=2)
        start_page_button.grid(column=0, row=i+2)

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
    workouts_df.save_to_csv("logWorkouts.csv")

    # Close root window and display start page again. 
    root.destroy()
    display_start_page()
         

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

def display_set_goal(root):
    """
    Displays the start page of setting the goal. 
    The user can choose between 3 types of objectives that appears as buttons:
        Distance
        Duration
        Calories burned
    After clicking each button a new page is displayed.

    Parameters
    ----------
    root : tkinter.Window
        The root window of the GUI for GymGenie.
    """
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()
        
    #Create the frame
    goals_frame = tk.Frame(root, bg=blue, pady=40)
    goals_frame.pack(fill=tk.BOTH, expand=True)
    goals_frame.columnconfigure(0, weight=1)
    goals_frame.rowconfigure(0, weight=1)
    goals_frame.rowconfigure(1, weight=1)
    goals_frame.rowconfigure(2, weight=1)
    goals_frame.rowconfigure(3, weight=1)
    goals_frame.rowconfigure(4, weight=1)

    #Create goal label
    goal_label = tk.Label(goals_frame, text="Set your goal based on:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)

    goal_label.grid(column=0, row=0)

    #Create goal buttons based on the type of objective
    GOALS_TYPES = ['Distance', 'Duration', 'Calories burned']
    commands = [lambda: display_distance(root), lambda: display_duration(root), lambda: display_calories(root)]
    for i, goal_type in enumerate(GOALS_TYPES):
        btn = tk.Button(goals_frame, 
            command= commands[i],
            text = goal_type, 
            font =("Arial", 12, "bold"),
            background=white,
            foreground=dark_blue,
            activebackground=light_blue,
            activeforeground=white,
            width=20,
            height=2, 
            border=0,
            cursor="hand2",
            borderwidth=1, #Add border width
            relief="solid") #Add relief style 

        btn.grid(column=0, row=1+i) 

    # Add exit button
    exit_button = gui.create_button(frame=goals_frame, command=lambda: exit(root),
                                    text = "Exit", width=5)
    exit_button.grid(column=0, row=4)

    
def display_duration(root):
    """
    Displays a new page with the parameters to set the duration goal.

    Parameters
    ----------
    root : tkinter.Window
        The root window of the GUI for GymGenie.

    """
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    #Create the main frame
    main_frame = tk.Frame(root, bg=blue, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)

    #Configure columns and rows
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)
    main_frame.columnconfigure(3, weight=1)
    main_frame.columnconfigure(4, weight=1)
    main_frame.columnconfigure(5, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    main_frame.rowconfigure(4, weight=1)

    #create duration label
    duration_label = tk.Label(main_frame, text="Duration:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=10,
            height = 1)
    duration_label.grid(column=0, row=0)

    #create h label
    h_label = tk.Label(main_frame, text="h",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)
    h_label.grid(column=2, row=0)
    
    #create min label
    min_label = tk.Label(main_frame, text="min",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)
    min_label.grid(column=4, row=0) 

    #create hours and minutes entry
    global e_hours
    e_hours = tk.Entry(main_frame)
    e_hours.insert(tk.END, 0)
    global e_min
    e_min = tk.Entry(main_frame)
    e_min.insert(tk.END, 0)
    e_hours.grid(column=1, row=0)
    e_min.grid(column=3, row=0)

    #Change boolean values to keep the workflow
    global set_duration
    set_duration = True

    #Display other common parameters: timeframe, timescale, type of exercise, save button and smart tips.
    display_timeframe(main_frame , col = 0 , row = 1 )
    display_exercise_type(main_frame)
    display_smarttips(main_frame)
    display_timescale(main_frame)
    display_save_button(main_frame, root)

    # Add exit button
    exit_button = gui.create_button(frame=main_frame, command=lambda: exit(root),
                                    text = "Exit", width=5)
    exit_button.grid(column=4, row=4)




def display_distance(root):
    """
    Displays a new page with the parameters to set the distance goal.

    Parameters
    ----------
    root : tkinter.Window
        The root window of the GUI for GymGenie.
    
    """
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    #Create the main frame
    main_frame = tk.Frame(root, bg=blue, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)

    #Configure columns and rows
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)
    main_frame.columnconfigure(3, weight=1)
    main_frame.columnconfigure(4, weight=1)
    main_frame.columnconfigure(5, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    main_frame.rowconfigure(4, weight=1)

    #create distance label
    distance_label = tk.Label(main_frame, text="Distance:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)
    distance_label.grid(column=0, row=0)

    #create entry
    global e_distance
    e_distance= tk.Entry(main_frame)
    e_distance.insert(tk.END, 0)
    e_distance.grid(column=1, row=0)
    #create option menu
    distance_units = ["km", "m","miles"]
    global selected_unit_distance
    selected_unit_distance = tk.StringVar(main_frame)
    selected_unit_distance.set(distance_units[0])
    distance_units_options = tk.OptionMenu(main_frame, selected_unit_distance, *distance_units) 
    distance_units_options.grid(column=2, row=0)

    #Change boolean values to keep the workflow
    global set_distance
    set_distance = True

    #Display other common parameters: timeframe, timescale, type of exercise, save button and smart tips.
    display_timeframe(main_frame , col = 0 , row = 1 )
    display_exercise_type(main_frame)
    display_smarttips(main_frame)
    display_timescale(main_frame)
    display_save_button(main_frame, root)

    # Add exit button
    exit_button = gui.create_button(frame=main_frame, command=lambda: exit(root),
                                    text = "Exit", width=5)
    exit_button.grid(column=4, row=4)


def display_calories(root):
    """
    Displays a new page with the parameters to set the calories goal.

    Parameters
    ----------
    root : tkinter.Window
        The root window of the GUI for GymGenie.
    
    """
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    #Create the main frame
    main_frame = tk.Frame(root, bg=blue, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)

    #Configure columns and rows
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)
    main_frame.columnconfigure(3, weight=1)
    main_frame.columnconfigure(4, weight=1)
    main_frame.columnconfigure(5, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    main_frame.rowconfigure(4, weight=1)

    #create duration label
    calories_label = tk.Label(main_frame, text="Calories burned:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)
    calories_label.grid(column=0, row=0)

    #create entry
    global e_calories
    e_calories = tk.Entry(main_frame)
    e_calories.insert(tk.END, 0)
    e_calories.grid(column=1, row=0)
    #create option menu
    calories_units = ["kcal", "kJ"]
    global selected_unit_calories
    selected_unit_calories = tk.StringVar(main_frame)
    selected_unit_calories.set(calories_units[0])
    calories_units_options = tk.OptionMenu(main_frame, selected_unit_calories, *calories_units) 
    calories_units_options.grid(column=2, row=0)

    #Change boolean values to keep the workflow
    global set_calories
    set_calories = True

    #Display other common parameters: timeframe, timescale, type of exercise, save button and smart tips.
    display_timeframe(main_frame , col = 0 , row = 1 )
    display_exercise_type(main_frame)
    display_smarttips(main_frame)
    display_timescale(main_frame)
    display_save_button(main_frame, root)

    # Add exit button
    exit_button = gui.create_button(frame=main_frame, command=lambda: exit(root),
                                    text = "Exit", width=5)
    exit_button.grid(column=4, row=4)



def display_timeframe(main_frame, col , row):
    """
    Displays the timeframe label and its entries to set the start and end dates.

    Args:
        main_frame : frame where to be displayed.
        col (int) : column number of the grid of the actual frame.
        row (int) : row number of the grid of the actual frame.
    
    """
    #create timeframe, start and end label
    timeframe_label = tk.Label(main_frame, text="Timeframe:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)
    
    start_button = tk.Button(main_frame, text="Start",
                    font =("Arial", 12, "bold"),
                    background=white,
                    foreground=black,
                    width=20,
                    height = 1,
                    command=lambda: gui.open_calendar(root, start_date))
    
    end_button = tk.Button(main_frame, text="End",
                font =("Arial", 12, "bold"),
                background=white,
                foreground=black,
                width=20,
                height = 1,
                command=lambda: gui.open_calendar(root, end_date))

    #Create start date 
    global start_date
    start_date = tk.StringVar()
    start_date.set(datetime.date.today()) # Set the date initial date to todays date.
    start_date_label = tk.Label(main_frame,
                font =("Arial", 12, "bold"),
                background=blue,
                foreground=white,
                width=20,
                height = 1, 
                textvariable=start_date)
    
    #Create end date 
    global end_date
    end_date = tk.StringVar()
    end_date.set(datetime.date.today() + datetime.timedelta(days=1)) # Set the date initial date to todays date.
    end_date_label = tk.Label(main_frame,
                font =("Arial", 12, "bold"),
                background=blue,
                foreground=white,
                width=20,
                height = 1, 
                textvariable=end_date)
    
    #Configure columns and rows and display widgets
    timeframe_label.grid(column=col, row=row)
    start_button.grid(column=col+1, row=row)
    start_date_label.grid(column=col+2, row=row)
    end_button.grid(column=col+3, row=row)
    end_date_label.grid(column=col+4, row=row)




def display_exercise_type(main_frame):
    """
    Displays the workout label and an option menu to choose which type of exercise the goal is related to.

    Parameters
    ----------
    main_frame : tkinter.frame where to be placed.
        
    """
    #Create label
    exercise_label = tk.Label(main_frame, 
                        text="Workout:",
                        font =("Arial", 14, "bold"),
                        background=blue,
                        foreground=white,
                        width=20,
                        height = 1)
    exercise_label.grid(column=0 , row = 4)

    # Create list containing the names of all the workout types of class Workout.
    workout_types = [subclass.__name__ for subclass in workout.Workout.__subclasses__()]

    # Variable to keep track of the option 
    # selected in OptionMenu 
    global selected_workout
    selected_workout = tk.StringVar(main_frame) 

    # Set the default value of the variable 
    selected_workout.set("Select") 

    # Create the optionmenu widget and passing the workout_types and the selected_wotkout to it. 
    question_menu = tk.OptionMenu(main_frame, selected_workout, *workout_types, ) 
    question_menu.grid(column = 2, row = 4) 


def display_smarttips(main_frame, col = 3, row = 3):
    """
    Displays the SMART tips button and the pop up message.

    Args:
        main_frame : frame where to be displayed.
        col (int) : column number of the grid of the actual frame.
        row (int) : row number of the grid of the actual frame.
    
    """
    #Create button
    tip_button = tk.Button(main_frame, text="SMART TIP", command=popup_smarttips,
                           width= 15, height=10,
                            activebackground=yellow, 
                            activeforeground="white",
                            anchor="center",
                            bd=3,
                            bg='turquoise1',
                            cursor="hand2",
                            disabledforeground=light_blue,
                            fg="black",
                            font=("Tahoma", 12, "bold"),
                            highlightbackground="black",
                            highlightcolor="green",
                            highlightthickness=2,
                            justify="center",
                            overrelief="raised")
    tip_button.grid(column=col, row=row, columnspan=2)



def popup_smarttips():
    """
    It creates a message box that contains a SMART tip randomly selected between a list of different statements.
    
    """
    TIPS = ["S - Specific: What will you achieve? ",
            "M - Measurable: What data will you use to decide whether you have met your goal?",
            "A - Achievable: Do you have the right skills to achieve this?",
            "A - Achievable: Are you sure you can do it?",
            "A - Achievable: Don't set goals where achieving lies in someone else’s power, it should be entirely down to you.",
            "R - Relevant: Does the goal align with those of your team or organization?",
            "T - Time bound: What is the deadline for accomplishing the goal?What is the deadline for accomplishing the goal?"]
    tk.messagebox.showinfo("BE SMART !", random.choice(TIPS))


def display_timescale(main_frame):
    """
    Displays time-scale and option menu to set a goal as weekly, monthly or yearly.

    Parameters
    ----------
    main_frame : tkinter.frame where to be placed.

    """
    #create timescale label
    timescale_label = tk.Label(main_frame, text="Time-scale:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)
    timescale_label.grid(column=0, row=3)

    #create days label
    timescale_label = tk.Label(main_frame, text="days",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)
    timescale_label.grid(column=2, row=3)

    #create option menu
    options = [7, 30,365]
    global selected_timescale
    selected_timescale = tk.StringVar(main_frame)
    #Set default variable
    selected_timescale.set(options[0])
    scale_options = tk.OptionMenu(main_frame, selected_timescale, *options) 
    scale_options.grid(column=1, row=3)


def display_save_button(main_frame, root):
    """
    Displays a save button. When the user clicks on it the goals are saved on a dataframe and exported as csv file.

    Parameters
    ----------
    root : tkinter.Window
        The root window of the GUI for GymGenie.

    main_frame : tkinter.frame where to be placed.
    
    """
    #Add save button
    save_btn = tk.Button(main_frame, 
        command= lambda: save_goal(main_frame, root) ,
        text = "save", 
        font =("Arial", 12, "bold"),
        background=white,
        foreground=dark_blue,
        activebackground=light_blue,
        activeforeground=white,
        width=10,
        height=1, 
        border=0,
        cursor="hand2",
        borderwidth=1, #Add border width
        relief="solid") #Add relief style
    save_btn.grid(column=3, row=4)


def save_goal(main_frame, root):  
    """
    Saves the user input goal data.

    Parameters
    ----------
    root : tkinter.Window
        The root window of the GUI for GymGenie.

    main_frame : tkinter.frame where to be placed.
    
    """

    #Give format to dates to be able to add to the dataframe
    start_date_tmp = start_date.get().split('-')
    start_date_value = Date(int(start_date_tmp[0]), int(start_date_tmp[1]), int(start_date_tmp[2]))

    end_date_tmp = end_date.get().split('-')
    end_date_value = Date(int(end_date_tmp[0]), int(end_date_tmp[1]), int(end_date_tmp[2]))

    #Create goal object
    if set_distance:
        current_goal = goal.Goal(value=int(e_distance.get()), unit = selected_unit_distance.get() ,time_scale=selected_timescale.get(), 
                           start_date=start_date_value, end_date=end_date_value, exercise=selected_workout.get())
    
    elif set_duration: 
        #create duration object
        current_duration = Duration(int(e_hours.get()), int(e_min.get()))
        current_goal = goal.DurationGoal(value=current_duration.minutes ,time_scale=selected_timescale.get(), 
                           start_date=start_date_value, end_date=end_date_value, exercise=selected_workout.get())

    elif set_calories:
        current_goal = goal.Goal(value=int(e_calories.get()), unit = selected_unit_calories.get() ,time_scale=selected_timescale.get(), 
                           start_date=start_date_value, end_date=end_date_value, exercise=selected_workout.get())
    print(current_goal)


    # Check if a goals dataframe already exists. If not, create one.
    current_directory = os.getcwd().replace(os.sep,'/')
    goals_file = current_directory + "/goals.csv"
    try:
        goals_df_data = pd.read_csv(goals_file)
        goals_df = dataframe.GoalDataframe()
        goals_df.data = goals_df_data
    except FileNotFoundError:
        goals_df = dataframe.GoalDataframe()

    # Add the goal object to the dataframe and save as csv file
    goals_df.add_goal(current_goal)

    # Save dataframe in a file csv
    goals_df.save_dataframe("goals.csv")

    # Close root window and display start page again. 
    root.destroy()
    display_start_page()


#run it
display_start_page()