# Change 1: Abstraction of the Dataframe Class

We applied the prinicple of abstraction in our code when creating the class Dataframe, with subclasses for dataframes of workouts or of goals. At first, we only created a specific class for the dataframe of workouts. But when working on the functionality of setting goals, we noticed that the structures required to save them and a lot of the functionalities, like saving the dataframe, editing or deleting entries, are very similar what we implemented for the dataframe of workouts. Only details differ between the two classes, like the column names the dataframe needs and what information is passed to create a new entry. So, we restructured our code for the Dataframe class to be more generic and added the more detailed functions to the subclasses.

# Change 2: Decomposition of the main program

We used some decomposition on a coarse level when designing the main program. The components are all the main functionalities our program should have, like logging a new workout, setting a goal or showing the progress, and each of them was put into their own function. The functions are wrapped together in the main program to create the full logic for the user experience.

# Change 3: Plot Goal and Progress

In task 2, we needed to produce some plot about the goal and the workouts. For each type of plot we did a different function because they are all independent from each other and in this way we kept clean the structure of our code.

# Change 4: GUI

In parallel we implemented a GUI. The user will be able to choose if they wants to interact with the terminal or with the GUI made with Tkinter. Each window and functionality needed a function to be implemented, using all the object created in the last task.

# Change 5: Abstraction of GUI functions

When implementing our GUI, we discovered we repeat many of the same settings when we are making a new widget. Therefore, we created functions for creating a frame, button, labels etc. that have default values we often use, but still have the flexibility to change the widgets by allowing kwargs into the functions as well. These functions are in their own module.
