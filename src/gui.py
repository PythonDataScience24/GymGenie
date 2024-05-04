import tkinter as tk
import workout

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

def create_button(frame, command, text, font, width, height):
    button = tk.Button(
        frame,
        command=command,
        text=text,
        font=font,
        background=dark_blue,
        foreground=white,
        activebackground=light_blue,
        activeforeground=white,
        width=width,
        height=height, 
        border=0,
        cursor="hand2"
    )
    return button

def display_start_page():
    """
    Displays the startpage of the workout-application where the user can choose to log a workout,
    set a new goal, look at the overview of their goals or look at the trends in their workouts.
    """
    root = tk.Tk()
    root.geometry("500x400")
    #root.resizeable(width=False, height=False) # in case we want to keep a constant size of the window
    root.title("GymGenie")

    main_frame = tk.Frame(root, bg=blue, pady=30)
    main_frame.pack(fill=tk.BOTH, expand=True)
    main_frame.columnconfigure(0, weight=1)
    for i in range(5):
        main_frame.rowconfigure(i, weight=1)

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

    start_page_buttons = [("Log a workout", lambda: choose_workout(root)), 
                          ("Set a new goal", lambda: set_goal(root)),
                          ("View goals", lambda: view_goals(root)), 
                          ("View progress and trends", lambda: view_progress_and_trends(root))]

    for i, button in enumerate(start_page_buttons):
        start_page_button = create_button(frame=main_frame, command=button[1],
                                          text=button[0], font=("Arial", 12, "bold"), 
                                          width=20, height=2)
        start_page_button.grid(column=0, row=i+1)

    tk.mainloop()

def choose_workout(root):
    for widget in root.winfo_children():
        widget.destroy()
        
    choose_workout_frame = tk.Frame(root, bg=blue, pady=20)
    choose_workout_frame.pack(fill=tk.BOTH, expand=True)
    choose_workout_frame.columnconfigure(0, weight=1)
    number_workout_types = len(workout.Workout.__subclasses__())
    for i in range(number_workout_types+1):
        choose_workout_frame.rowconfigure(i, weight=1)

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

    workout_types = [subclass.__name__ for subclass in workout.Workout.__subclasses__()]

    for i, workout_type in enumerate(workout_types):
        choose_workout_button = create_button(frame=choose_workout_frame, command=None,
                                            text=workout_type, font=("Arial", 10, "bold"), 
                                            width=20, height=1)
        choose_workout_button.grid(column=0, row=i+1)

def set_goal(root):
    for widget in root.winfo_children():
        widget.destroy()

    set_goal_frame = tk.Frame(root, bg=blue, pady=40) # frame can be renamed so it fits best with your code.
    set_goal_frame.pack(fill=tk.BOTH, expand=True) 
    

def view_goals(root):
    for widget in root.winfo_children():
        widget.destroy()

    view_goal_frame = tk.Frame(root, bg=blue, pady=40) # same here for renaming
    view_goal_frame.pack(fill=tk.BOTH, expand=True)

def view_progress_and_trends(root):
    for widget in root.winfo_children():
        widget.destroy()

    progress_trend_frame = tk.Frame(root, bg=blue, pady=40)
    progress_trend_frame.pack(fill=tk.BOTH, expand=True)

display_start_page()