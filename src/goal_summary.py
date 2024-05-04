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
        #print(goalDataframe)
        #print(index_list)
        #print(len(index_list))
        if len(index_list) > 0:
            return index_list[0]
        else:
            return None

    # plot goal using barplot
    def plot_goal(self,time_frame, start_time, end_time,exercise):
        """
        This function shows the plot of the progress through the goal

        """
        # plot General goal for week/month/year
        # plot Specific Exercise for week/month/year
        # retrieve the index goal
        index_goal = self.findGoal(time_frame,start_time,end_time,exercise)
        if index_goal == None:
            return "Goal not found!"
        print(index_goal)
        # find the value of the goal
        value_goal = self.goalDataframe.iloc[[index_goal]]['value'].item()
        unit_value = self.goalDataframe.iloc[[index_goal]]['unit'].item()
        print(value_goal)
        print(unit_value)
        # convert value in standard km, maybe we set up only goals in km
        #if unit_value == "miles":
        #    converted_distance = distance.Distance(value_goal,unit_value)
        #    converted_distance.distance_convert(unit_value, "km")
        #    value_goal = converted_distance.print_distance()

        # filter the logWorkout dataframe, containing only all the activities with the same exercise
        # and according to the timeframe
        print(self.logWorkoutDataframe)
        filtered_workout_dataframe = self.logWorkoutDataframe[(self.logWorkoutDataframe['activity'] == exercise) & 
                                                               (self.logWorkoutDataframe['date'] >= start_time) &
                                                               (self.logWorkoutDataframe['date'] <= end_time)]
        print(filtered_workout_dataframe)
        # convert all distance in standard km? not necessary for the moment
        # create a bar plot (Usin the bar to shows the goal attribute for each session)
        # add an horizontal line to shows where the goal is
        match unit_value:
            case "kcal":
                plt.bar(filtered_workout_dataframe['date'], filtered_workout_dataframe['calories'], edgecolor='gray')
                ylabel = "Calories"
            case "km":
                plt.bar(filtered_workout_dataframe['date'], filtered_workout_dataframe['distance'],edgecolor='gray')
                ylabel = "Distance"
            case "min":
                plt.bar(filtered_workout_dataframe['date'], filtered_workout_dataframe['duration'],edgecolor='gray')
                ylabel = "Duration"
        # add goal line in the barplot
        plt.axhline(value_goal, linestyle='--', lw=1.2,color='black', label="Goal", zorder=-1.5)
        plt.ylabel(ylabel, fontsize=12)
        plt.xticks(rotation=-25, fontsize=8)
        #plt.xlabel('Time', fontsize=12)
        plt.legend(frameon=False)
        plt.title(exercise)
        plt.show()

        return True

        # return the plot
    # plot using progress pie chart to shows what is left
    # TODO


if __name__=="__main__":

    logWork = pd.DataFrame({'activity': ['Running','Cycling','Running','Swimming','Running'], 'date': [date(2024,4,20),date(2024,4,21),date(2024,4,22),date(2024,4,23),date(2024,4,24)] , 'duration' : [40,120,30,20,20],
                                    'distance' : [9,40,6,2,8], 'calories' : [200,500,250,400,300], 'rating' : [8,9,4,5,6]})

    goalFrame = pd.DataFrame({"value":[35,100], "unit":['min','km'], "time_scale":[7,7], "start_date":[date(2024,4,20),date(2024,5,20)], 
                                "end_date":[date(2024,4,24), date(2024,5,24)], "exercise":['Running','Cycling']})

    summary = GoalSummary(logWork,goalFrame)

    print(summary.plot_goal(7,date(2024,4,20), date(2024,4,24), 'Running'))
