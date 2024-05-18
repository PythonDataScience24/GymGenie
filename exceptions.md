We implemented try and except statements in the different functions that get the input from the user. It is important to not let the program "fail in silence", which would make it hard for the user to find out what went wrong. Instead, it is better to return an type of "default" value that is returned in case of an error, or raise an exception to stop the program from running before it enters computationally expensive tasks with wrong input.


## Example 1: Exception handling for user input
 For example in the file goal_summary.py for the methods get_timescale(), get_quantity(), and get_exercises(). We try to convert the input to an integer in get_timescale(), or check if it is contained in a list of valid inputs for the other two methods. If it is, the input is returned, otherwise a message to enter valid input is printed, and the user is asked for his input again.

 ## Example 2: Exception handling when opening files
 In the main.py file, we use a try-except statement when opening the files with previously logged workouts or set goals. This exception handler is specific to the FileNotFoundError, because in the specific case that no such file exists previously, for example because a user uses the application for the first time, we want the program to just create a new, empty dataframe, but not crash.