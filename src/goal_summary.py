import pandas as pd
import distance
from datetime import date
import matplotlib.pyplot as plt
class GoalSummary:
    """
    This class retrives the goal for each esercise and plot the current situation, showing what is left

    Attributes:
    TODO

    """

    def __init__(self, logWorkoutDataframe, goalDataframe):
        """
        Initialize a GoalSummary object
        """
        self.logWorkoutDataframe = logWorkoutDataframe
        self.goalDataframe = goalDataframe


    def findGoal(self, time_frame, start_time, end_time, exercise):
        """
        This function find the unique goal in the dataframe
        """
        goalDataframe = self.goalDataframe
        index_list = goalDataframe.index[(goalDataframe['time_scale'] == time_frame) & (goalDataframe['start_date'] == start_time) & 
                                (goalDataframe['end_date'] == end_time) & (goalDataframe['exercise'] == exercise)].tolist()
        if len(index_list) > 0:
            return index_list[0]
        else:
            return 0

    # plot goal using barplot
    def plot_goal(self,time_frame, start_time, end_time,exercise):
        """
        This function shows the plot of the progress through the goal

        """
        # retrieve the index goal
        index_goal = self.findGoal(time_frame,start_time,end_time,exercise)
        if index_goal == 0:
            return "Goal not found!"
        print(index_goal)
        # find the value of the goal
        value_goal = self.goalDataframe.iloc[[index_goal]]['value']
        unit_value = self.goalDataframe.iloc[[index_goal]]['unit']
        print(value_goal)
        print(unit_value)
        # convert value in standard km, maybe we set up only goals in km
        #if unit_value == "miles":
        #    converted_distance = distance.Distance(value_goal,unit_value)
        #    converted_distance.distance_convert(unit_value, "km")
        #    value_goal = converted_distance.print_distance()

        # filter the logWorkout dataframe, containing only all the activities with the same exercise
        # and according to the timeframe
        filtered_workout_dataframe = self.logWorkoutDataframe[(self.logWorkoutDataframe['exercise'] == exercise) & 
                                                               (self.logWorkoutDataframe['date'] >= start_time |
                                                               self.logWorkoutDataframe['date'] <= end_time)]
        print(filtered_workout_dataframe)
        # convert all distance in standard km? not necessary for the moment
        # create a bar plot (Usin the bar to shows the goal attribute for each session)
        # add an horizontal line to shows where the goal is
        match unit_value:
            case "kcal":
                plt.bar(filtered_workout_dataframe['date'], filtered_workout_dataframe['calories'])
                ylabel = "Calories"
            case "km":
                plt.bar(filtered_workout_dataframe['date'], filtered_workout_dataframe['distance'])
                ylabel = "Distance"
            case "min":
                plt.bar(filtered_workout_dataframe['date'], filtered_workout_dataframe['duration'])
                ylabel = "Duration"
        # add goal line in the barplot
        plt.hlines(value_goal, linestyles='--', lw=2,colors='black')
        plt.ylabel(ylabel)
        plt.show()

        return True

        # return the plot
    # plot using progress pie chart to shows what is left
    # TODO


if __name__=="__main__":

    logWork = pd.DataFrame({'activity': ['Running','Cycling','Running','Swimming','Running'], 'date': [date(2024,4,20),date(2024,4,21),date(2024,4,22),date(2024,4,23),date(2024,4,24)] , 'duration' : [40,120,30,20,20],
                                    'distance' : [9,40,6,2,8], 'calories' : [200,500,250,400,300], 'rating' : [8,9,4,5,6]})

    goalFrame = pd.DataFrame({"value":[300,100], "unit":['min','km'], "time_scale":[7,7], "start_date":[date(2024,4,20),date(2024,5,20)], 
                                "end_date":[date(2024,4,24), date(2024,5,24)], "exercise":['Running','Cycling']})

    summary = GoalSummary(logWork,goalFrame)

    summary.plot_goal(7,date(2024,4,20), date(2024,4,24), 'Running')
