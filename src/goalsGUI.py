import tkinter as tk

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



def display_set_goal():
    """
    Displays the start page of setting the goal. 
    The user can choose between 3 types of objectives that appears as buttons:
        Distance
        Duration
        Calories burned
    
    """

    root = tk.Tk()
    root.geometry("500x400")

    #Create the main frame
    main_frame = tk.Frame(root, bg=blue, pady=40)
    main_frame.pack(fill=tk.BOTH, expand=True)
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1)
    main_frame.rowconfigure(3, weight=1)
    main_frame.rowconfigure(4, weight=1)


    #Create goal label
    goal_label = tk.Label(main_frame, text="Set your goal based on:",
                        font =("Arial", 16, "bold"),
            background=blue,
            foreground=white,
            width=20,
            height = 1)

    goal_label.grid(column=0, row=0)

    #Create goal buttons based on the type of objective
    GOALS_TYPES = ['Distance', 'Duration', 'Calories burned']
    for i, goal_type in enumerate(GOALS_TYPES):
        btn = tk.Button( main_frame, 
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
            relief="solid") #Add relief style # I've read that with Tkinter you can not change the color o fthe buttons :(

        
        btn.grid(column=0, row=1+i) 


    root.mainloop()

