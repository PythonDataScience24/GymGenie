import tkinter as tk
import numpy as np
import os
import pandas as pd
import workout
import tkcalendar
import datetime
import dataframe
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

def create_frame(root, **kwargs):
    """
    Creates a frame with customizable properties.

    Parameters
    ----------
    root : tkinter.Tk or tkinter.Toplevel
        The root or top-level window in which the frame should be placed.

    **kwargs : dict, optional
        Additional keyword arguments to customize the frame.
        Supported keyword arguments include:
            - bg: Background color of the frame (default is "blue")
            - pady: Padding in the y-direction (default is 20)
            - rows: Number of rows to configure in the frame (default is 1)
            - columns: Number of rows to configure in the frame (default is 1)

    Returns
    -------
    frame : tkinter.Frame
        The created frame widget.
    """
    # Default values
    bg = kwargs.get("bg", blue)
    pady = kwargs.get("pady", 20)
    rows = kwargs.get("rows", 1)
    columns = kwargs.get("columns", 1)

    # Create frame
    frame = tk.Frame(root, bg=bg, pady=pady)
    frame.pack(fill=tk.BOTH, expand=True)

    # Configure rows
    for i in range(rows):
        frame.rowconfigure(i, weight=1)

    # Configure columns
    for i in range(columns):
        frame.columnconfigure(i, weight=1)

    return frame


def create_button(frame, command, text, **kwargs):
    """
    Creates a button with customizable properties.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame in which the button should be placed.

    command : function
        A function for what should happen when the button is clicked.

    text : str
        The text that should be displayed on the button.

    **kwargs : dict, optional
        Additional keyword arguments to customize the button.
        Supported keyword arguments include:
            - font: Tuple specifying the font (default is ("Arial", 12, "bold"))
            - width: Width of the button (default is 20)
            - height: Height of the button (default is 1)
            - background: Background color of the button (default is dark blue)
            - foreground: Foreground color of the button (default is white)
            - activebackground: Background color of the button when active (default is light blue)
            - activeforeground: Foreground color of the button when active (default is white)
            - border: Border width of the button (default is 0)
            - cursor: Cursor style when hovering over the button (default is "hand2")

    Returns
    -------
    button : tkinter.Button
        The created button widget.
    """
    # Default values
    font = kwargs.get("font", ("Arial", 12, "bold"))
    width = kwargs.get("width", 20)
    height = kwargs.get("height", 1)
    background = kwargs.get("background", dark_blue)
    foreground = kwargs.get("foreground", "white")
    activebackground = kwargs.get("activebackground", light_blue)
    activeforeground = kwargs.get("activeforeground", "white")
    border = kwargs.get("border", 0)
    cursor = kwargs.get("cursor", "hand2")

    button = tk.Button(
        frame,
        command=command,
        text=text,
        font=font,
        background=background,
        foreground=foreground,
        activebackground=activebackground,
        activeforeground=activeforeground,
        width=width,
        height=height,
        border=border,
        cursor=cursor
    )
    return button

def create_entry(frame, **kwargs):
    """
    Creates an entry widget with customizable properties.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame in which the entry should be placed.

    **kwargs : dict, optional
        Additional keyword arguments to customize the entry.
        Supported keyword arguments include:
            - font: Tuple specifying the font (default is ("Arial", 10, "normal"))
            - background: Background color of the entry (default is white)
            - foreground: Foreground color of the entry (default is black)
            - width: Width of the entry (default is 10)
            - show: Character to be displayed in place of the input (default is None)
            - textvariable: Tkinter variable to associate with the entry (default is None)

    Returns
    -------
    entry : tkinter.Entry
        The created entry widget.
    """
    # Default values
    font = kwargs.get("font", ("Arial", 10, "normal"))
    background = kwargs.get("background", "white")
    foreground = kwargs.get("foreground", "black")
    width = kwargs.get("width", 15)
    show = kwargs.get("show", None)
    textvariable = kwargs.get("textvariable", None)

    entry = tk.Entry(
        frame,
        font=font,
        background=background,
        foreground=foreground,
        width=width,
        show=show,
        textvariable=textvariable
    )
    return entry

def create_label(frame, **kwargs):
    """
    Creates a label widget with customizable properties.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame in which the label should be placed.

    **kwargs : dict, optional
        Additional keyword arguments to customize the label.
        Supported keyword arguments include:
            - text: String of the text to be displayed on the label.
            - textvariable: tkinter.StringVar to associate with the label's text.
            - font: Tuple specifying the font (default is ("Arial", 10, "bold"))
            - background: Background color of the label (default is blue)
            - foreground: Foreground color of the label (default is white)
            - width: Width of the label (default is 10)
            - height: Height of the label (default is 1)

    Returns
    -------
    label : tkinter.Label
        The created label widget.
    """
    # Default values
    text = kwargs.get("text", "")
    textvariable = kwargs.get("textvariable", None)
    font = kwargs.get("font", ("Arial", 10, "bold"))
    background = kwargs.get("background", blue)
    foreground = kwargs.get("foreground", white)
    width = kwargs.get("width", 10)
    height = kwargs.get("height", 1)

    label = tk.Label(
        frame,
        text=text,
        textvariable=textvariable,
        font=font,
        background=background,
        foreground=foreground,
        width=width,
        height=height
    )
    return label

def create_scale(frame, **kwargs):
    """
    Creates a Scale widget with customizable properties.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame in which the scale should be placed.

    **kwargs : dict, optional
        Additional keyword arguments to customize the scale.
        Supported keyword arguments include:
            - from_: The starting value of the scale.
            - to: The ending value of the scale.
            - resolution: The resolution of the scale.
            - variable: The tkinter variable associated with the scale.
            - orient: Orientation of the scale ('horizontal' or 'vertical').
            - length: Length of the scale widget.
            - command: Function to be called when the scale value changes.
            - bg: Background color of the scale.
            - fg: Foreground color of the scale.

    Returns
    -------
    scale : tkinter.Scale
        The created Scale widget.
    """
    # Default values
    from_ = kwargs.get('from_', 1)
    to = kwargs.get('to', 10)
    resolution = kwargs.get('resolution', 1)
    variable = kwargs.get('variable', None)
    orient = kwargs.get('orient', 'horizontal')
    length = kwargs.get('length', 100)
    command = kwargs.get('command', None)
    bg = kwargs.get('bg', None)
    fg = kwargs.get('fg', None)

    # Create the scale widget
    scale = tk.Scale(frame, from_=from_, to=to, resolution=resolution, variable=variable,
                     orient=orient, length=length, command=command, bg=bg, fg=fg)
    return scale

def create_option_menu(frame, options, selected_option, **kwargs):
    """
    Creates an OptionMenu widget with customizable properties.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame in which the OptionMenu should be placed.

    options : list
        List of options for the dropdown menu.

    selected_option : tkinter.StringVar
        Variable to store the selected option.

    command : function, optional
        Function to be called when an option is selected (default is None).

    **kwargs : dict, optional
        Additional keyword arguments to customize the OptionMenu.
        Supported keyword arguments include:
            - command : Function to be called when an option is selected (default is None).
            - font: Tuple specifying the font (default is ("Arial", 10, "bold"))
            - background: Background color of the OptionMenu (default is None)
            - foreground: Foreground color of the OptionMenu (default is None)
            - width: Width of the OptionMenu (default is None)
            - height: Height of the OptionMenu (default is None)

    Returns
    -------
    option_menu : tkinter.OptionMenu
        The created OptionMenu widget.
    """
    # Default values
    command = kwargs.get("command", None)
    font = kwargs.get("font", ("Arial", 10, "bold"))
    background = kwargs.get("background", None)
    foreground = kwargs.get("foreground", None)
    width = kwargs.get("width", None)
    height = kwargs.get("height", None)

    # Create the OptionMenu widget
    option_menu = tk.OptionMenu(frame, selected_option, *options, **kwargs)

    return option_menu

def open_calendar(root, date):
    """
    Opens a new window where you can choose a date and updates the provided date variable with the 
    chosen date.

    Parameters
    ----------
    root : tkinter.Tk or tkinter.Toplevel
        The root or top-level window where the calendar window will be opened.

    date : tkinter.StringVar
        A tkinter StringVar variable that stores the selected date.
    """


    date_window = tk.Toplevel(root)
    date_window.title("Pick a Date")

    calendar = tkcalendar.Calendar(date_window)
    calendar.pack(padx=10, pady=10)

    confirm_button = tk.Button(date_window, text="Confirm", command=lambda: select_date(date, calendar, date_window))
    confirm_button.pack(pady=10)

def select_date(date, calendar, date_window):
    """
    Updates the provided Tkinter variable with the selected date from a calendar widget.

    Parameters
    ----------
    date : tkinter.StringVar
        The Tkinter variable to be updated with the selected date.

    calendar : tkcalendar.Calendar
        The calendar widget used for selecting the date.

    date_window : tkinter.Toplevel
        The window containing the calendar widget.
    """
    selected_date = calendar.selection_get()
    date.set(selected_date)
    date_window.destroy()

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
    duration = Duration(hours=hours_entry.get(), minutes=minutes_entry.get())
    print(duration)
    date = selected_date.get()
    if distance_entry in globals():
        distance = Distance(distance=distance_entry.get(), unit=selected_unit_distance.get())
    else:
        distance = np.nan

    # Create a workout object and store it in a dataframe format.
    workout_type = getattr(workout, workout_type)
    my_workout = workout_type(calories=calories, rating=rating, duration=duration, date=date, distance=distance)

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
    main_frame = create_frame(root=root, rows=5)

    # Add welcome label
    welcome_label = create_label(frame=main_frame, text = "Welcome to GymGenie!", 
                                 font =("Arial", 16, "bold"), width=20)
    welcome_label.grid(column=0, row=0)

    # Initialize list of buttons containing the button-text and which command should be executed 
    # when the button is clicked.
    start_page_buttons = [("Log a workout", lambda: choose_workout(root)), 
                          ("Set a new goal", lambda: set_goal(root)),
                          ("View goals", lambda: view_goals(root)), 
                          ("View progress and trends", lambda: view_progress_and_trends(root))]

    # Create and place the buttons on the main frame.
    for i, button in enumerate(start_page_buttons):
        start_page_button = create_button(frame=main_frame, command=button[1],
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
    rows= len(workout.Workout.__subclasses__()) + 1 # include all workout types + one label
    choose_workout_frame = create_frame(root=root, rows=rows)   

    # Add label that asks for the type of workout.
    label = create_label(frame=choose_workout_frame, text = "What type of workout did you do?",
                         font =("Arial", 14, "bold"), width=40)
    label.grid(column=0, row=0)

    # Create list containing the names of all the workout types of class Workout.
    workout_types = [subclass.__name__ for subclass in workout.Workout.__subclasses__()]

    # Create a button for each workout type with a command that let's the user log the workout.
    for i, workout_type in enumerate(workout_types):
        choose_workout_button = create_button(frame=choose_workout_frame, 
                                              command=lambda: log_workout(workout_type),
                                              text=workout_type)
        choose_workout_button.grid(column=0, row=i+1)

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
    rows=len(workout_datatypes)+2 # include all datatypes + title and save-button

    # Create frame where you can choose log in all the dta from your workout.    
    log_workout_frame = create_frame(root=root, pady=10, columns=5, rows=rows)

    # Add top-label for the log workout-page
    log_workout_label = create_label(frame=log_workout_frame, text="Log your workout:",
                                     font=("Arial", 16, "bold"))
    log_workout_label.grid(column=1, row=0, columnspan=3, sticky="ew")

    # Create widgets for entering the workout data.
    for i, workout_datatype in enumerate(workout_datatypes):
        # Create labels for each datatype that should be inputed and place them in the first column.
        datatype_label = create_label(frame=log_workout_frame, text = f"{workout_datatype}:")
        datatype_label.grid(column=0, row=i+1, sticky="e")

        # Calories: insert an entry and a dropdown menu with options for the unit.
        if workout_datatype == "Calories":
            global calories_entry
            calories_entry = create_entry(frame=log_workout_frame)
            calories_entry.grid(column=1, row=i+1)
            calories_units = ["kcal", "kJ"]

            global selected_unit_calories 
            selected_unit_calories = tk.StringVar(root)
            selected_unit_calories.set(calories_units[0])
            calories_units_options = create_option_menu(frame=log_workout_frame, options=calories_units,
                                                       selected_option=selected_unit_calories) 
            calories_units_options.grid(column=2, row=i+1)       

        # Distance: insert an entry and a dropdown menu with options for the unit.
        if workout_datatype == "Distance":
            global distance_entry
            distance_entry = create_entry(log_workout_frame)
            distance_entry.grid(column=1, row=i+1)

            global selected_unit_distance
            distance_units = ["km", "m", "miles"]
            selected_unit_distance = tk.StringVar(root)
            selected_unit_distance.set(distance_units[0])
            distance_units_options = create_option_menu(frame=log_workout_frame, options=distance_units,
                                                       selected_option=selected_unit_distance) 
            distance_units_options.grid(column=2, row=i+1)

        # Rating: insert slider and label describing the scale
        if workout_datatype == "Rating":
            global rating_slider
            rating_slider = create_scale(frame=log_workout_frame)
            rating_slider.grid(column=1, row=i+1)
            rating_label = create_label(frame=log_workout_frame, text="Rate workout: 1=Easy, 10=Hard")
            rating_label.grid(column=2, row=i+1, columnspan=2, sticky="ew")


        # Duration: insert an entry and a label specifying the unit (min)
        if workout_datatype == "Duration":
            global hours_entry
            hours_entry = create_entry(log_workout_frame)
            hours_entry.grid(column=1, row=i+1)
            hours_label = create_label(frame=log_workout_frame, text="hours")
            hours_label.grid(column=2, row=i+1, sticky="w")

            global minutes_entry
            minutes_entry = create_entry(log_workout_frame)
            minutes_entry.grid(column=3, row=i+1)
            minutes_label = create_label(frame=log_workout_frame, text="minutes")
            minutes_label.grid(column=4, row=i+1, sticky="w")
            

        # Date: insert a label with the date and a button that allows user to choose the date.
        if workout_datatype == "Date":
            global selected_date
            selected_date = tk.StringVar()
            selected_date.set(datetime.date.today()) # Set the date initial date to todays date.
            date_label = create_label(frame=log_workout_frame, textvariable=selected_date)
            date_label.grid(column=1, row=i+1)
            calendar_button = create_button(frame=log_workout_frame, 
                                            command= lambda: open_calendar(root, selected_date),
                                            text="Select a date", font=("Arial", 10, "bold"), width=12)
            calendar_button.grid(column=2, row=i+1)
    
    # Add save-button(save all the logged data put in by the user) at the bottom of the page.
    save_button = create_button(frame=log_workout_frame, text="Save", width=15,
                                command=lambda: save_data(frame=log_workout_frame, 
                                                          workout_type=workout_type))
    save_button.grid(columns=5, row=len(workout_datatypes)+1)
         

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

display_start_page()