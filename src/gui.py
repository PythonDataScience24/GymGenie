import tkinter as tk

black = "WHITE"
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
    root = tk.Tk()
    root.geometry("500x400")
    #root.resizeable(width=False, height=False) # in case we want to keep a constant size of the window
    root.title("GymGenie")

    main_frame = tk.Frame(root, bg=blue, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    main_frame.rowconfigure(4, weight=1)

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

    log_workout_button = tk.Button(
        main_frame, 
        text = "Log a workout",
        font =("Arial", 12, "bold"),
        background=dark_blue,
        foreground=white,
        activebackground=light_blue,
        activeforeground=white,
        width=20,
        height=2, 
        border=0,
        cursor="hand2"
    )
    log_workout_button.grid(column=0, row=1)

    log_workout_button = tk.Button(
        main_frame, 
        text = "Set a new goal",
        font =("Arial", 12, "bold"),
        background=dark_blue,
        foreground=white,
        activebackground=light_blue,
        activeforeground=white,
        width=20,
        height=2, 
        border=0,
        cursor="hand2"
    )

    log_workout_button.grid(column=0, row=2)

    log_workout_button = tk.Button(
        main_frame, 
        text = "View goals",
        font =("Arial", 12, "bold"),
        background=dark_blue,
        foreground=white,
        activebackground=light_blue,
        activeforeground=white,
        width=20,
        height=2, 
        border=0,
        cursor="hand2"
    )
    log_workout_button.grid(column=0, row=3)

    log_workout_button = tk.Button(
        main_frame, 
        text = "View progress and trends",
        font =("Arial", 12, "bold"),
        background=dark_blue,
        foreground=white,
        activebackground=blue,
        activeforeground=white,
        width=20,
        height=2, 
        border=0,
        cursor="hand2"
    )
    log_workout_button.grid(column=0, row=4)


    #lbl_welcome = tk.Label(root, text="Welcome to GymGenie!")
    #lbl_welcome.pack()

    #btn_logWorkout = tk.Button(root, text="Log a workout", command=lambda: chooseWorkout(root))
    #btn_logWorkout.pack()
 
    #btn_setGoal = tk.Button(root, text="Set a new goal")
    #btn_setGoal.pack()

    #btn_overviewGoals = tk.Button(root, text="Overview of your goals")
    #btn_overviewGoals.pack()

    #btn_quit = tk.Button(root, text="Quit")
    #btn_quit.pack()

    tk.mainloop()

def chooseWorkout(start_window):
    """
    Allows the user to chose the type of workout they want to log.
    """
    start_window.destroy()
    type_window = tk.Tk()
    tk.Label(type_window, text="Choose a type of workout").pack()
    
    for type in WORKOUT_TYPES:
        tk.Button(type_window, text=type, command=lambda: logWorkout(type_window)).pack()


def logWorkout(type_window):
    """
    Allows the user to log a type of workout.
    """
    type_window.destroy()
    log_window = tk.Tk()
    tk.Label(log_window, text="Log a workout").pack()

display_start_page()