import tkinter as tk
#from PIL import ImageTk, Image #You need to install Pillow
import tkcalendar #Installing is needed
from tkinter import messagebox
import goal
import datetime
import workout
import random
from calories import Calories
from date import Date
from distance import Distance
from duration import Duration
from date import Date
import dataframe
import os
import pandas as pd


#color palette
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


#root = tk.Tk()
#root.geometry("500x400")

### Global variables
#Create boolean values to keep the workflow
global set_distance
set_distance = False
global set_duration
set_duration = False
global set_calories
set_calories = False

#####
#Other functions (need to be on top)
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



def display_set_goal(root):
    """
    Displays the start page of setting the goal. 
    The user can choose between 3 types of objectives that appears as buttons:
        Distance
        Duration
        Calories burned
    After clicking each button a new page is displayed.
    
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
    


def display_duration(root):
    """
    Displays a new page with the parameters to set the duration goal.

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
            width=20,
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

    #Display other common parameters: timeframe, type of exercise and smart tips.
    display_timeframe(main_frame , col = 0 , row = 1 )
    display_exercise_type(main_frame)
    display_smarttips(main_frame)
    display_timescale(main_frame)
    display_save_button(main_frame, root)




def display_distance(root):
    """
    Displays a new page with the parameters to set the distance goal.
    
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

    display_timeframe(main_frame , col = 0 , row = 1 )
    display_exercise_type(main_frame)
    display_smarttips(main_frame)
    display_timescale(main_frame)
    display_save_button(main_frame, root)


def display_calories(root):
    """
    Displays a new page with the parameters to set the calories goal.
    
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

    display_timeframe(main_frame , col = 0 , row = 1 )
    display_exercise_type(main_frame)
    display_smarttips(main_frame)
    display_timescale(main_frame)
    display_save_button(main_frame, root)



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
    
    start_button = tk.Button(main_frame, text="Start date",
                    font =("Arial", 12, "bold"),
                    background=white,
                    foreground=black,
                    width=20,
                    height = 1,
                    command=lambda: open_calendar(root, start_date))
    
    end_button = tk.Button(main_frame, text="End date",
                font =("Arial", 12, "bold"),
                background=white,
                foreground=black,
                width=20,
                height = 1,
                command=lambda: open_calendar(root, end_date))

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
    #Create label
    exercise_label = tk.Label(main_frame, 
                        text="Type of workout:",
                        font =("Arial", 16, "bold"),
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
    question_menu.grid(column = 1, row = 4) 


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
    tip_button.grid(column=col, row=row)



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
    save_btn.grid(column=2, row=4)




def save_goal(main_frame, root):  

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


    # Check if a workout dataframe already exists. If not, create one.
    current_directory = os.getcwd().replace(os.sep,'/')
    goals_file = current_directory + "/goals.csv"
    try:
        goals_df_data = pd.read_csv(goals_file)
        goals_df = dataframe.GoalDataframe()
        goals_df.data = goals_df_data
    except FileNotFoundError:
        goals_df = dataframe.GoalDataframe()

    # Add the workout object to the dataframe and save as csv file
    goals_df.add_goal(current_goal)

    # Save dataframe in a file csv
    goals_df.save_dataframe("goals.csv")

    # Close root window and display start page again. 
    root.destroy()



#run it
#display_set_goal()








#root.mainloop()






#NOTES FOR ME

#Commands for img
# my_img = ImageTk.PhotoImage(Image.open(""))
# my_img.pack()