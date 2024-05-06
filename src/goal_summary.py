import pandas as pd
import numpy as np
import distance,date,dur
import matplotlib.pyplot as plt
class GoalSummary:
    """
    This class retrives the goal for each esercise and plot the current situation, showing what is left

    Attributes:
    TODO

    """

    def __init__(self, log_workout_dataframe:pd.DataFrame, goal_data_frame:pd.DataFrame):
        """
        Initialize a GoalSummary object
        """
        self.log_workout_dataframe = log_workout_dataframe
        self.goal_data_frame = goal_data_frame


    def find_goal(self, time_frame:int, start_time:date.Date, end_time:date.Date, exercise:str):
        """
        This function find the unique goal in the dataframe
        """
        index_list = self.goal_data_frame.index[(self.goal_data_frame['time_scale'] == time_frame) & 
                                         (self.goal_data_frame['start_date'] == start_time) & 
                                            (self.goal_data_frame['end_date'] == end_time) & 
                                            (self.goal_data_frame['exercise'] == exercise)].tolist()
        #print(type(start_time))
        #print(index_list)
        #print(len(index_list))
        if len(index_list) > 0:
            return index_list[0]
        else:
            return None

    # plot goal using barplot
    def plot_goal(self,time_frame:int, start_time:date.Date, end_time:date.Date,exercise:str,type:str):
        """
        This function shows the plot of the progress through the goal

        """
        # plot General goal for week/month/year
        # plot Specific Exercise for week/month/year
        # retrieve the index goal
        index_goal = self.find_goal(time_frame,start_time,end_time,exercise)
        if index_goal == None:
            return "Goal not found!"
        print(index_goal)
        # find the value of the goal
        value_goal = self.goal_data_frame.iloc[[index_goal]]['value'].item()
        unit_value = self.goal_data_frame.iloc[[index_goal]]['unit'].item()
        print(value_goal)
        print(unit_value)
        # DO NOT DELETE YET
        # convert value in standard km, maybe we set up only goals in km
        #if unit_value == "miles":
        #    converted_distance = distance.Distance(value_goal,unit_value)
        #    converted_distance.distance_convert(unit_value, "km")
        #    value_goal = converted_distance.print_distance()

        # Case 1: Specific Exercise
        if type in ["Running", "Cycling", "Strength", "Swimming", "Walking", "Skiing", "Climbing", "Others"]:

            self.plot_specific_exercise(self.log_workout_dataframe,exercise,start_time,end_time,unit_value)
        else:
            print("print me")
            # plot progression
            self.plot_progression(self.log_workout_dataframe, unit_value, value_goal)
            # plot general workout
            self.plot_general_workout(self.log_workout_dataframe, unit_value)
            # plot total workout left to reach the goal
            self.plot_percentage(self.log_workout_dataframe, unit_value, value_goal)



    def plot_specific_exercise(self,workout_datafram:pd.DataFrame, exercise:str,start_time:date.Date,end_time:date.Date, unit_value:str):
        """
        This function plot for every specific workout activity the progress
        made towards the specific goal
        Attributes:
        TODO
        """
        # filter the logWorkout dataframe, containing only all the activities with the same exercise
        # and according to the timeframe
        filtered_workout_dataframe = workout_datafram[(workout_datafram['activity'] == exercise) & 
                                                               (workout_datafram['date'] >= start_time) &
                                                               (workout_datafram['date'] <= end_time)]
        print(filtered_workout_dataframe)
        # convert all distance in standard km? not necessary for the moment TODO

        # create a bar plot according to which type of goal we wants to visualize
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
        plt.ylabel(ylabel, fontsize=12)
        plt.xticks(rotation=-25, fontsize=8)
        plt.legend(frameon=False)
        plt.title(exercise)
        plt.tight_layout()
        plt.show()

    def plot_progression(self, dataframe:pd.DataFrame, unit_value:str, value_goal:int):
        """
        This function shows the total progression made towards these goal
        Attribute:
        TODO
        """
        # Depending on the unit choosen in the goal dataframe select different column
        match unit_value:
            case "kcal":
                unit = 'calories'
            case "km":
                unit = 'distance'
            case "min":
                unit = 'duration'
        # Group date according to the unit choosen
        # If there are more workout in one day it will sum the unit according
        progression = dataframe.groupby('date')[unit].sum().reset_index()
        print(progression)
        # create a new column called progress and use the function cumsum
        # that will do partial sum of the row before
        progression['progression'] = progression[unit].cumsum().fillna(progression[unit][0])
        # draw the bar plot with the progression
        plt.bar(progression['date'], progression['progression'], color="red")
        # add the label of the partial sum on the top of the bar
        plt.bar_label(plt.bar(progression['date'], progression['progression'], color='red'),progression['progression'])
        # Adjust the ylim to have a 'space' after the goal line : Check that is valid for all the cases
        plt.ylim(0,value_goal + 50)
        # Draw the horizontal line showing the goal
        plt.axhline(value_goal, linestyle='--', lw=1.2,color='black', label="Goal", zorder=-1.5)
        plt.ylabel(unit.capitalize(), fontsize=12)
        plt.xticks(rotation=25, fontsize=8)
        plt.tight_layout()
        plt.legend(frameon=False)
        #plt.show()

    def plot_general_workout(self, dataframe:pd.DataFrame, unit_value:str):
        """
        This function shows the different types of exercise did every day with different color
        Arguments
        TODO
        """
        # Depending on the unit choosen in the goal dataframe select different column
        match unit_value:
            case "kcal":
                unit = 'calories'
            case "km":
                unit = 'distance'
            case "min":
                unit = 'duration'
        # group each day every sport
        grouped_dataframe = dataframe.groupby(['activity', 'date']).sum().reset_index()
        # create a pivot table
        pivot_df = grouped_dataframe.pivot(index='date', columns='activity', values=unit)
        print(pivot_df)
        # draw the pivot table
        pivot_df.plot(kind='bar',stacked=True)
        # Adding labels on top of each bar
        # it adds also the 0, not good!
        #for container in ax.containers:
        #    print(container.pchanged())
        #    print(container.get_label())
        #    ax.bar_label(container, label_type='center')
        plt.xlabel("")
        plt.ylabel(unit_value)
        plt.xticks(rotation=25)
        plt.legend(title='Activity', frameon=False)
        plt.tight_layout()
        plt.show()
    

    def plot_percentage(self, dataframe:pd.DataFrame, unit_value:str, value_goal:int):
        """
        This function plot the a pie chart with the marked workout done towards the goal.
        If the goal has been reached, the pie chart will be color full otherwise only the part
        that has been completed with the percentage
        Attribute
        TODO
        """
        # Depending on the unit choosen in the goal dataframe select different column
        match unit_value:
            case "kcal":
                unit = 'calories'
            case "km":
                unit = 'distance'
            case "min":
                unit = 'duration'
        # Group date according to the unit choosen
        # If there are more workout in one day it will sum the unit according
        progression = dataframe.groupby('date')[unit].sum().reset_index()
        # plot using progress pie chart to shows what is left
        # find th total workout
        total_sum = progression[unit].sum()
        if total_sum >= value_goal:
            # if goal has been reached the pie chart will be complete
            percentage_left = round(total_sum)
            slices = [percentage_left]
        else:
            # if the goal has NOT been reached the pie chart wont be completed
            percentage_left = round((total_sum/value_goal)*100)
            slices = [total_sum,round(value_goal-total_sum)]
        
        # draw the pie chart
        plt.pie(slices, colors=['green'],startangle=90, counterclock=False)
        # add a circle in the middle to draw a donut
        my_circle=plt.Circle( (0,0), 0.7, color='white')
        p=plt.gcf()
        p.gca().add_artist(my_circle)
        plt.text(0,0,f"{percentage_left} %",verticalalignment='center', horizontalalignment='center', fontsize=35, fontname="fantasy")
        plt.title(f"Total Progress {unit.capitalize()}")
        plt.show()




if __name__=="__main__":

    logWork = pd.DataFrame({'activity': ['Running','Cycling','Cycling','Running','Swimming','Running'], 'date': [date.Date(2024,4,20).get_date(), date.Date(2024,4,20).get_date(),date.Date(2024,4,21).get_date(),date.Date(2024,4,22).get_date(),date.Date(2024,4,23).get_date(),date.Date(2024,4,24).get_date()] , 'duration' : [40,80,120,30,20,20],
                                    'distance' : [9,50,40,6,2,8], 'calories' : [200,300,500,250,400,300], 'rating' : [8,7,9,4,5,6]})

    goalFrame = pd.DataFrame({"value":[300,100], "unit":['min','km'], "time_scale":[7,7], "start_date":[date.Date(2024,4,20).get_date(),date.Date(2024,5,20).get_date()], 
                                "end_date":[date.Date(2024,4,24).get_date(), date.Date(2024,5,24).get_date()], "exercise":['Running','Cycling']})

    summary = GoalSummary(logWork,goalFrame)

    print(summary.plot_goal(7,date.Date(2024,4,20).get_date(), date.Date(2024,4,24).get_date(), 'Running', np.NaN))
    
