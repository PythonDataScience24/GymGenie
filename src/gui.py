import tkinter as tk
import workout
import numpy as np
import tkcalendar
import datetime

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
            - width: Width of the button (default is 0)
            - height: Height of the button (default is 0)
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
    width = kwargs.get("width", 0)
    height = kwargs.get("height", 0)
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
    width = kwargs.get("width", 10)
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

def create_label(frame, text, **kwargs):
    """
    Creates a label widget with customizable properties.

    Parameters
    ----------
    frame : tkinter.Frame
        The frame in which the label should be placed.

    text : str
        The text to be displayed on the label.

    **kwargs : dict, optional
        Additional keyword arguments to customize the label.
        Supported keyword arguments include:
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
    font = kwargs.get("font", ("Arial", 10, "bold"))
    background = kwargs.get("background", blue)
    foreground = kwargs.get("foreground", white)
    width = kwargs.get("width", 10)
    height = kwargs.get("height", 1)

    label = tk.Label(
        frame,
        text=text,
        font=font,
        background=background,
        foreground=foreground,
        width=width,
        height=height
    )
    return label

def open_calendar(root, date):
    """
    Opens a new window where you can choose a date and returns the chosen date.

    Returns
    -------
    date : 

    """
    def select_date(date):
        selected_date = calendar.selection_get()
        date.set(selected_date)
        date_window.destroy()
        return date

    date_window = tk.Toplevel(root)
    date_window.title("Pick a Date")

    calendar = tkcalendar.Calendar(date_window)
    calendar.pack(padx=10, pady=10)

    confirm_button = tk.Button(date_window, text="Confirm", command=lambda: select_date(date))
    confirm_button.pack(pady=10)

def display_start_page():
    """
    Displays the startpage of the workout-application where the user can choose to log a workout,
    set a new goal, look at the overview of their goals or look at the trends in their workouts.
    """

    # Create root window
    root = tk.Tk()
    root.geometry("500x400")
    #root.resizeable(width=False, height=False) # in case we want to keep a constant size of the window
    root.title("GymGenie")

    # Create frame for the main page
    main_frame = tk.Frame(root, bg=blue, pady=30)
    main_frame.pack(fill=tk.BOTH, expand=True)
    main_frame.columnconfigure(0, weight=1)
    for i in range(5): # configure 5 rows: one for a label and 4 for buttons
        main_frame.rowconfigure(i, weight=1)

    # Add welcome label
    label = tk.Label(
        main_frame, 
        text = "Welcome to GymGenie!",
        font =("Arial", 16, "bold"),
        background=blue,
        foreground=white,
        width=20,
        height = 1
    )
    label.grid(column=0, row=0)

    # Initialize list of buttons containing the button-text and which command should be executed 
    # when the button is clicked.
    start_page_buttons = [("Log a workout", lambda: choose_workout(root)), 
                          ("Set a new goal", lambda: set_goal(root)),
                          ("View goals", lambda: view_goals(root)), 
                          ("View progress and trends", lambda: view_progress_and_trends(root))]

    # Create and place the buttons on the main frame.
    for i, button in enumerate(start_page_buttons):
        start_page_button = create_button(frame=main_frame, command=button[1],
                                          text=button[0], font=("Arial", 12, "bold"), 
                                          width=20, height=2)
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
    choose_workout_frame = tk.Frame(root, bg=blue, pady=20)
    choose_workout_frame.pack(fill=tk.BOTH, expand=True)
    choose_workout_frame.columnconfigure(0, weight=1)
    number_workout_types = len(workout.Workout.__subclasses__())
    for i in range(number_workout_types+1): # include all workout types and one label for the number of rows.
        choose_workout_frame.rowconfigure(i, weight=1)

    # Add label that asks for the type of workout.
    label = tk.Label(
    choose_workout_frame, 
    text = "What type of workout did you do?",
    font =("Arial", 14, "bold"),
    background=blue,
    foreground=white,
    width=40,
    height = 1
    )
    label.grid(column=0, row=0)

    # Create list containing the names of all the workout types of class Workout.
    workout_types = [subclass.__name__ for subclass in workout.Workout.__subclasses__()]

    # Create a button for each workout type with a command that let's the user log the workout.
    for i, workout_type in enumerate(workout_types):
        choose_workout_button = create_button(frame=choose_workout_frame, 
                                              command=lambda subclass=workout_type: log_workout(root, subclass),
                                              text=workout_type, font=("Arial", 10, "bold"), 
                                              width=20, height=1)
        choose_workout_button.grid(column=0, row=i+1)

def log_workout(root, workout_type):
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

    # Create frame where you can choose log in all the dta from your workout.    
    log_workout_frame = tk.Frame(root, bg=blue, pady=10)
    log_workout_frame.pack(fill=tk.BOTH, expand=True)
    log_workout_frame.columnconfigure(0, weight=1)
    log_workout_frame.columnconfigure(1, weight=1)
    log_workout_frame.columnconfigure(2, weight=1)

    workout_type = getattr(workout, workout_type)
    workout_datatypes_dict = vars(workout_type())
    workout_datatypes_dict = {key: value for key, value in workout_datatypes_dict.items() if not np.isnan(value)}
    workout_datatypes = workout_datatypes_dict.keys()

    number_of_datatypes = len(workout_datatypes_dict.values())
    for i in range(number_of_datatypes+1): # include all datatypes and one label for the number of rows.
        log_workout_frame.rowconfigure(i, weight=1)


    # Create an entry for each of the datatypes:
    for i, workout_datatype in enumerate(workout_datatypes):
        workout_datatype = workout_datatype.capitalize()
        label = tk.Label(
        log_workout_frame, 
        text = f"{workout_datatype}:",
        font =("Arial", 10, "bold"),
        background=blue,
        foreground=white,
        width=10,
        height = 1
        )
        label.grid(column=0, row=i+1, sticky="e")
        if workout_datatype == "Calories":
            calories_entry = create_entry(log_workout_frame)
            calories_entry.grid(column=1, row=i+1)

        if workout_datatype == "Distance":
            distance_entry = create_entry(log_workout_frame)
            distance_entry.grid(column=1, row=i+1)
        if workout_datatype == "Rating":
            rating_entry = create_entry(log_workout_frame)
            rating_entry.grid(column=1, row=i+1)
        if workout_datatype == "Duration":
            duration_entry = create_entry(log_workout_frame)
            duration_entry.grid(column=1, row=i+1)
        if workout_datatype == "Date":
            date = tk.StringVar()
            date.set(datetime.date.today())
            
            current_date_label.grid(column=1, row=i+1)
            calendar_button = create_button(log_workout_frame, command= lambda: open_calendar(root, date),
                                            text="Select a date", font=("Arial", 10, "bold"),
                                            width=15, height=1)
            calendar_button.grid(column=2, row=i+1)

         

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