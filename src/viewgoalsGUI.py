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
from dataframe import WorkoutDataframe 
import goal_summary



root = tk.Tk()
root.geometry("500x400")

def view_goals(root):
    # Remove all widgets from the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Create frame for the page where the user can view the goals
    view_goal_frame = tk.Frame(root, bg=blue, pady=40) 
    view_goal_frame.pack(fill=tk.BOTH, expand=True)

    #read workout.csv and goals.csv
    goals_df = pd.read_csv("goals.csv")
    workout_df = pd.read_csv("logWorkouts.csv")

    #create GoalSummary object
    current_goalsummary = goal_summary.GoalSummary(workout_df, goals_df)

    #