import pandas as pd

class GoalDataframe():
    def __init__(self, column_names):
        self.data = pd.DataFrame(columns = column_names)

    #function to create a dataframe?
    #function to edit dataframe

    #function to save it

    #function to print it
    #function to add a goal(row)

if __name__ == "__main__":
    column_names = ["value", "unit", "time_scale", "start_date", "end_date", "exercise"]
    my_goals_df = GoalDataframe(column_names)