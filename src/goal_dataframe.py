import pandas as pd
import goal, date, duration

class GoalDataframe():
    """
    Class of a dataframe containing several Goals.

    Attributes:
        data: the Dataframe containing the goals as rows.
    """
    def __init__(self):
        self.data = pd.DataFrame(columns = ["value", "unit", "time_scale", "start_date", "end_date", "exercise"])

    def add_goal(self, goal: goal.Goal):
        """
        Add a new goal as a new row to the dataframe.
        """
        self.data = pd.concat([self.data, pd.DataFrame({"value":[goal.value], "unit":[goal.unit], "time_scale":[goal.time_scale], "start_date":[goal.start_date], "end_date":[goal.end_date], "exercise":[goal.exercise]})])

        #make sure duplicated entries are not possible
        if sum(self.data.duplicated()) > 0:
            print("This goal is already present in the table, the second entry will be dropped.")
            self.data.drop_duplicates(inplace = True)
    
    def save_dataframe(self, path: str):
        """
        Save the dataframe to a specified path.
        """
        self.data.to_csv(path)

    def print_dataframe(self):
        """
        Print the dataframe contained in the data attribute of the object.
        """
        print(self.data)
    
    def edit_dataframe(self, column_name: str, row_idx: int, new_value):
        """
        Edit a specific cell of the dataframe.

        Args:
            column_name (str): Name of the column in which an entry should be edited.
            row_idx (int): Index of the row in which an entry should be edited.
            new_value: The value to be newly assigned to the specified entry.
        """
        self.data.loc[row_idx, column_name] = new_value
    
    def delete_entry(self, row_idx: int):
        """
        Delete a row (one entry) of the dataframe.
        
        Args:
        row_idx (int): Index of the row that should be removed.
        """
        self.data.drop(row_idx)
    

if __name__ == "__main__":
    my_goals_df = GoalDataframe()
    print(my_goals_df)

    #create a goal to store in the dataframe
    my_start_date = date.Date(2024, 5, 3, 0, 0)
    my_end_date = date.Date(2024, 10, 31, 0 ,0)
    my_duration = duration.Duration(hours = 5)
    my_duration_goal = goal.DurationGoal(value = my_duration, time_scale = 7, start_date = my_start_date.print(), end_date = my_end_date.print())
    my_duration = duration.Duration(minutes = 90)
    my_duration_goal = goal.DurationGoal(value = my_duration, time_scale = 7, start_date = my_start_date, end_date = my_end_date)

    my_goals_df.add_goal(my_duration_goal)
    my_goals_df.print_dataframe()
    
    my_goals_df.add_goal(my_duration_goal)

    my_goals_df.edit_dataframe("value", 0, duration.Duration(minutes = 120))
    my_goals_df.print_dataframe()