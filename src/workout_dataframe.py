import pandas as pd

class Workout_dataframe:
    """
    Represents a Dataframe  that contains the information from the user.

    """
    def __init__(self, exercise, date, duration, distance, calories, rating):
        self.exercise = exercise
        self.date = date
        self.duration = duration
        self.distance = distance
        self.calories = calories
        self.rating = rating
    
    def create_dataframe(self): #need to be tested, confused in exercise/workout
        """
        Create a new dataframe with the columns:
            exercise 
            date
            duration
            distance
            calories
            rating
        """
        self.dataframe = pd.DataFrame({'exercise': exercise, 'date': self.date , 'duration (min)' : self.duration,
                                        'distance (km)' : self.distance, 'calories (kcal)' : self.calories, 'rating' : self.rating})
    
    def read_dataframe(self):
        """
        Print the dataframe created.

        """
        print(self.dataframe)
    
    def edit_dataframe(self, idx, column, new_value):
        """
        Edit the information of the desired column and desired idx of the dataframe.

        Args:
            idx (int) : index that refers to the desired row to be edited.(e.g. 'duration')
            column (str): desired column to be edited.(e.g. 'duration').
            new_value (int or str) : The new value to be assigned to the specified location.
        
        """
        self.dataframe.loc[idx , column] = new_value
    
    def save_dataframe(self, path):
        """
        Save the dataframe as csv file.

        Args:
            path : path that points where to save the dataframe.
        """
        self.dataframe.to_csv(path)


#test everything
#check names of attributes of classes