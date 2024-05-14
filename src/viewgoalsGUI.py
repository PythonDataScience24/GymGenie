import tkinter as tk
import numpy as np
import os
import pandas as pd
import random
import workout
import tkcalendar
import datetime
from tkinter import messagebox
from calories import Calories
from date import Date
from distance import Distance
from duration import Duration
from date import Date
from rating import Rating
from dataframe import WorkoutDataframe , GoalDataframe
import goal_summary
from tkinter import Canvas, Text
from gui import create_button, create_entry, create_label


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

root = tk.Tk()
root.geometry("500x400")

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



def view_goals(root):
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Create frame for the page where the user can view the goals
    view_goal_frame = tk.Frame(root, bg=blue) 
    view_goal_frame.pack(fill=tk.BOTH, expand=True)
    view_goal_frame.columnconfigure(0, weight=1)
    view_goal_frame.columnconfigure(1, weight=1)
    view_goal_frame.columnconfigure(2, weight=1)
    view_goal_frame.columnconfigure(3, weight=1)
    view_goal_frame.rowconfigure(0, weight=1)


    #read workout.csv and goals.csv
    #load the workouts from a pickle file, or start a dataframe to store them in if no file was found
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

    #create list of motivational messages
    messages = ["You're on the right track, keep going!", "You can either suffer the pain of discipline or the pain of regret", "You may not be there yet, but you are closer than you were yesterday", "Consistency is key - keep going", "One step at a time, one day at a time - you're getting closer!"]

    #create Canvas
    canvas_df = Canvas(root, bg=blue)
    canvas_df.pack()

    # Convert DataFrame to string representation
    goals_df_str = goals_df.data.to_string()

    # Create Text widget to display DataFrame
    text_widget = Text(canvas_df)
    text_widget.insert(tk.END, goals_df_str)
    text_widget.grid(column=0, row=0)

    # Create label to choose which goal to plot
    choose_label = create_label(view_goal_frame, text = "Check the progress on goal number (insert index): ", width=40)
    goal_row_entry = create_entry(view_goal_frame, width= 5)
    choose_label.grid(column=0, row=0, columnspan=2)
    goal_row_entry.grid(column=2, row=0)



    # transform the dataframe of workout and goals for plotting
    workouts_df.plot_dataframe()
    goals_df.plot_goals()

    #create GoalSummary object
    summary = goal_summary.GoalSummary(workouts_df, goals_df, messages)
    
    #Create plot button
    plot_btn = create_button(view_goal_frame, command= lambda: summary.plot_goal(goal_row_entry.get()) , text = "Plot", width =5 )
    plot_btn.grid(column=3, row=0)
    root.mainloop()

view_goals(root)

#def plot_button(root, frame):
