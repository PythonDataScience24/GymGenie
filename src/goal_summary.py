import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.figure import Figure
import seaborn as sns
import random
from date import Date
from distance import Distance
from duration import Duration
from dataframe import WorkoutDataframe
from calories import Calories
from rating import Rating
import matplotlib.dates as mdates


class GoalSummary:
    """
    This class retrieves the goal for each exercise and plots the current situation, 
    showing what is left.

    Attributes:
    log_workout_dataframe: The dataframe of the workouts of the user
    goal_data_frame: The dataframe of the goals of the user
    """

    def __init__(self, log_workout_dataframe: pd.DataFrame, goal_data_frame: pd.DataFrame, messages: list):
        """
        Initialize a GoalSummary object.
        """
        self.log_workout_dataframe = log_workout_dataframe
        self.goal_data_frame = goal_data_frame
        self.messages = messages
        self.fig = plt.figure()
        self.grid = gridspec.GridSpec(2, 2, height_ratios=[1, 1])

    def get_unit(self,unit_value:str):
        try:
            match unit_value:
                case "kcal":
                    unit = 'calories'
                case "km":
                    unit = 'distance'
                case "min":
                    unit = 'duration'
        except ValueError:
            print('Unit value incorrect entry!')
        return unit
    def plot_goal(self, index_goal):
        """
        This function shows the plot of the progress from the terminal through the goal.
        Args:
        index_goal: user selection of the goal to plot.
        """
        # plot General goal for week/month/year
        # plot Specific Exercise for week/month/year

        # Checks dataframe objects
        if self.log_workout_dataframe.data.empty or self.goal_data_frame.data.empty:
            print(
                'It seems that one of the dataframe has no data. Please add entry before seeing any plot!')
        else:
            # find the value of the goal
            value_goal = float(self.goal_data_frame.data.iloc[[
                               index_goal]]['value'].item())
            unit_value = self.goal_data_frame.data.iloc[[
                index_goal]]['unit'].item()
            exercise = self.goal_data_frame.data.iloc[[
                index_goal]]['exercise'].item()
            start_time = self.goal_data_frame.data.iloc[[
                index_goal]]['start_date'].item()
            end_time = self.goal_data_frame.data.iloc[[
                index_goal]]['end_date'].item()
            print(value_goal)
            print(unit_value)
            print(exercise)
            print(start_time)
            print(end_time)
            # DO NOT DELETE YET
            # convert value in standard km, maybe we set up only goals in km
            # if unit_value == "miles":
            #    converted_distance = distance.Distance(value_goal,unit_value)
            #    converted_distance.distance_convert(unit_value, "km")
            #    value_goal = converted_distance.print_distance()

            # Case 1: Specific Exercise
            if exercise in ["Running", "Cycling", "Strength", "Swimming", 
                        "Walking", "Skiing", "Climbing", "Others"]:

                return self.plot_specific_exercise(self.log_workout_dataframe, exercise, start_time, end_time, unit_value),self.plot_specific_exercise_percentage(self.log_workout_dataframe,exercise,unit_value,value_goal),None
            else:
                # plot progression
                return self.plot_progression(self.log_workout_dataframe, unit_value, value_goal),self.plot_general_workout(self.log_workout_dataframe, unit_value),self.plot_percentage(self.log_workout_dataframe, unit_value, value_goal)
                # plot general workout
                
                # plot total workout left to reach the goal
                


    def plot_specific_exercise(self, workout_dataframe: pd.DataFrame, exercise: str, start_time: Date, end_time: Date, unit_value: str):
        """
        This function plots for every specific workout activity the progress
        made towards the specific goal.
        Args:
        workout_dataframe: dataframe of the workouts of the user
        exercise: type of workout in which you want to achieve the goal. Default is None, to include all types of exercises
        start_time (Date): date at which the goals was set
        end_time (Date): date at which the goals should be reached
        unit_value: specific properties that the user wants to see (kcal,km or min)
        """
        # filter the logWorkout dataframe, containing only all the activities with the same exercise
        # and according to the timeframe
        workout_df = workout_dataframe.data
        workout_df['date'] = pd.to_datetime(workout_df['date'])
        filtered_workout_dataframe = workout_df[(workout_df['activity'] == exercise) &
                                                      (workout_df['date'] >= pd.to_datetime(start_time)) &
                                                      (workout_df['date'] <= pd.to_datetime(end_time))]
        # convert all distance in standard km? not necessary for the moment
        # create the figure
        fig = Figure(figsize=(5,5), dpi=100)
        ax = fig.add_subplot(111)
        # create a bar plot according to which type of goal we wants to visualize
        filtered_workout_dataframe['date'] = pd.to_datetime(filtered_workout_dataframe['date'])
        match unit_value:
            case "kcal":
                ax.bar(
                    filtered_workout_dataframe['date'], filtered_workout_dataframe['calories'], edgecolor='gray')
                ylabel = "Calories"
            case "km":
                ax.bar(
                    filtered_workout_dataframe['date'], filtered_workout_dataframe['distance'], edgecolor='gray')
                ylabel = "Distance"
            case "min":
                ax.bar(
                    filtered_workout_dataframe['date'], filtered_workout_dataframe['duration'], edgecolor='gray')
                ylabel = "Duration"
        print(pd.to_datetime(filtered_workout_dataframe['date']))
        # add an encouraging message to the plot
        #message_index = random.randrange(len(self.messages))
        #ax.subplots_adjust(bottom = 0.2)
        #ax.gcf().text(0.05, 0.05, self.messages[message_index], fontsize = 12)
        ax.set_ylabel(ylabel, fontsize=12)
        #ax.set_xticks(rotation=-25, fontsize=8)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.tick_params(axis='x', labelrotation=-25, labelsize=6)
        #ax.tick_params(axis='x',labelrotation=45, labelsize=8)
        # ax.legend(frameon=False)
        ax.set_title(exercise)
        #plt.show()

        return fig
    
    def plot_specific_exercise_percentage(self, dataframe: pd.DataFrame, exercise: str ,unit_value: str, value_goal: float):
        """
        This function plots a pie chart with the percentage of workouts done towards the goal.
        If the goal has been reached, the pie chart will be colored full, otherwise only the part
        that has been completed with the percentage.
        Args:
        dataframe: the dataframe of the workouts of the user
        unit_value: specific properties that the user wants to see (kcal, km or min)
        value_goal: the goal that the user wants to reach
        """
        # filter the logWorkout dataframe, containing only all the activities with the same exercise
        workout_df = dataframe.data
        # Depending on the unit choosen in the goal dataframe select different column
        unit = self.get_unit(unit_value)
        # Group date according to the unit choosen
        # If there are more workout in one day it will sum the unit accordingly
        progression = workout_df[workout_df['activity'] == exercise].groupby('date')[unit].sum().reset_index()
        print(progression)
        # plot using progress pie chart to shows what is left
        # find the total workout
        total_sum = progression[unit].sum()
        if total_sum >= value_goal:
            # if goal has been reached the pie chart will be complete
            percentage_left = round((total_sum/value_goal)*100)
            slices = [percentage_left]
            color = ['green']
        else:
            # if the goal has NOT been reached the pie chart wont be completed
            percentage_left = round((total_sum/value_goal)*100)
            slices = [percentage_left,100-percentage_left]
            color = ['green', 'white']
        print(slices)
        print(percentage_left)
        print(value_goal)
        fig = Figure(figsize=(5,5), dpi=100)
        ax = fig.add_subplot(111)
        # draw the pie chart
        ax.pie(slices, colors=color, startangle=90, counterclock=False, normalize=True)
        # add a circle in the middle to draw a donut
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        ax.text(0, 0, f"{percentage_left} %", verticalalignment='center',
                    horizontalalignment='center', fontsize=25, fontname="fantasy")
        ax.set_title(f"Total Progress {unit.capitalize()}")
        #plt.show()

        return fig

    def plot_progression(self, dataframe: pd.DataFrame, unit_value: str, value_goal: float):
        """
        This function shows the total progression made towards these goals
        Args:
        dataframe: the dataframe of the workouts of the user
        unit_value: specific properties that the user wants to see (kcal,km or min)
        value_goal: the goal that the user wants to reach
        """
        # Depending on the unit choosen in the goal dataframe select different column
        unit = self.get_unit(unit_value)
        # Group date according to the unit choosen
        # If there are more workout in one day it will sum the unit according
        progression = dataframe.data.groupby('date')[unit].sum().reset_index()
        print(progression)
        # create a new column called progress and use the function cumsum
        # that will do partial sum of the row before
        progression['progression'] = progression[unit].cumsum().fillna(
            progression[unit][0])
        # create the figure
        fig = Figure(figsize=(5,5), dpi=100)
        ax = fig.add_subplot(111)
        # draw the bar plot with the progression
        ax.bar(progression['date'], progression['progression'], color="red")
        # add the label of the partial sum on the top of the bar
        ax.bar_label(plt.bar(
            progression['date'], progression['progression'], color='red'), progression['progression'])
        # Adjust the ylim to have a 'space' after the goal line : Check that is valid for all the cases
        #ax.set_ylim(0, value_goal + 50)
        # Draw the horizontal line showing the goal
        ax.axhline(value_goal, linestyle='--', lw=1.2,
                    color='black', label="Goal", zorder=-1.5)
        # add an encouraging message to the plot
        message_index = random.randrange(len(self.messages))
        #plt.subplots_adjust(bottom = 0.2)
        #plt.gcf().text(0.05, 0.05, self.messages[message_index], fontsize = 12)
        ax.set_ylabel(unit.capitalize(), fontsize=12)
        ax.tick_params(axis='x',rotation=25, labelsize=8)
        ax.legend(frameon=False)
        #plt.show()

        return fig

    def plot_general_workout(self, dataframe: pd.DataFrame, unit_value: str):
        """
        This function shows the different types of exercise done every day with different colors.
        Args:
        dataframe: the dataframe of the workouts of the user
        unit_value: specific properties that the user wants to see (kcal,km or min)
        """
        # Depending on the unit choosen in the goal dataframe select different column
        unit = self.get_unit(unit_value)
        # group each day every sport
        grouped_dataframe = dataframe.data.groupby(
            ['activity', 'date']).sum().reset_index()
        # create a pivot table
        pivot_df = grouped_dataframe.pivot(
            index='date', columns='activity', values=unit)
        print(pivot_df)
        # draw the pivot table
        print(pivot_df.dtypes)
        # create the figure
        fig = Figure(figsize=(5,5), dpi=100)
        ax = fig.add_subplot(111)
        pivot_df.plot(kind='bar', ax=ax,stacked=True)
        # Adding labels on top of each bar
        # it adds also the 0, not good!
        # for container in ax.containers:
        #    print(container.pchanged())
        #    print(container.get_label())
        #    ax.bar_label(container, label_type='center')
        # add an encouraging message to the plot
        #message_index = random.randrange(len(self.messages))
        #plt.subplots_adjust(bottom = 0.2)
        #plt.gcf().text(0.05, 0.05, self.messages[message_index], fontsize = 12)
        ax.set_xlabel("")
        ax.set_ylabel(unit_value)
        ax.tick_params(axis='x',rotation=25, labelsize=8)
        ax.legend(title='Activity', frameon=False)
        #plt.show()

        return fig

    def plot_percentage(self, dataframe: pd.DataFrame, unit_value: str, value_goal: float):
        """
        This function plots the a pie chart with the percentage of workouts done towards the goal.
        If the goal has been reached, the pie chart will be colored full, otherwise only the part
        that has been completed with the percentage.
        Args:
        dataframe: the dataframe of the workouts of the user
        unit_value: specific properties that the user wants to see (kcal,km or min)
        value_goal: the goal that the user wants to reach
        """
        # Depending on the unit choosen in the goal dataframe select different column
        unit = self.get_unit(unit_value)
        # Group date according to the unit choosen
        # If there are more workout in one day it will sum the unit according
        progression = dataframe.data.groupby('date')[unit].sum().reset_index()
        # plot using progress pie chart to shows what is left
        # find th total workout
        total_sum = progression[unit].sum()
        if total_sum >= value_goal:
            # if goal has been reached the pie chart will be complete
            percentage_left =  round((total_sum/value_goal)*100)
            colors = ['green']
            slices = [percentage_left]
        else:
            # if the goal has NOT been reached the pie chart wont be completed
            percentage_left = round((total_sum/value_goal)*100)
            slices = [percentage_left, 100-percentage_left]
            colors = ['green', 'white']

        # create the figure
        fig = Figure(figsize=(5,5), dpi=100)
        ax = fig.add_subplot(111)
        # draw the pie chart
        ax.pie(slices, colors=colors, startangle=90, counterclock=False)
        # add a circle in the middle to draw a donut
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        ax.text(0, 0, f"{percentage_left} %", verticalalignment='center',
                 horizontalalignment='center', fontsize=35, fontname="fantasy")
        ax.set_title(f"Total Progress {unit.capitalize()}")
        #plt.show()

        return fig

    # plot goal using barplot
    def plot_goal_terminale(self, index_goal):
        """
        This function shows the plot of the progress through the goal
        Args:
        index_goal: user selection of the goal to plot.
        """

        # plot General goal for week/month/year
        # plot Specific Exercise for week/month/year

        # Checks dataframe objects
        if self.log_workout_dataframe.data.empty or self.goal_data_frame.data.empty:
            print(
                'It seems that one of the dataframe has no data. Please add entry before seeing any plot!')
        else:
            # find the value of the goal
            value_goal = float(self.goal_data_frame.data.iloc[[
                               index_goal]]['value'].item())
            unit_value = self.goal_data_frame.data.iloc[[
                index_goal]]['unit'].item()
            exercise = self.goal_data_frame.data.iloc[[
                index_goal]]['exercise'].item()
            start_time = self.goal_data_frame.data.iloc[[
                index_goal]]['start_date'].item()
            end_time = self.goal_data_frame.data.iloc[[
                index_goal]]['end_date'].item()
            print(value_goal)
            print(unit_value)
            print(exercise)
            print(start_time)
            print(end_time)
            # DO NOT DELETE YET
            # convert value in standard km, maybe we set up only goals in km
            # if unit_value == "miles":
            #    converted_distance = distance.Distance(value_goal,unit_value)
            #    converted_distance.distance_convert(unit_value, "km")
            #    value_goal = converted_distance.print_distance()

            # Case 1: Specific Exercise
            if exercise in ["Running", "Cycling", "Strength", "Swimming", 
                        "Walking", "Skiing", "Climbing", "Others"]:

                self.plot_specific_exercise_terminale(
                    self.log_workout_dataframe, exercise, start_time, end_time, unit_value)
                self.plot_specific_exercise_percentage_terminale(self.log_workout_dataframe,exercise,unit_value,value_goal)
            else:
                # plot progression
                self.plot_progression_terminale(
                    self.log_workout_dataframe, unit_value, value_goal)
                # plot general workout
                self.plot_general_workout_terminale(
                    self.log_workout_dataframe, unit_value)
                # plot total workout left to reach the goal
                self.plot_percentage_terminale(
                    self.log_workout_dataframe, unit_value, value_goal)

    def plot_specific_exercise_terminale(self, workout_datafram: pd.DataFrame, exercise: str, start_time: Date, end_time: Date, unit_value: str):
        """
        This function plot for every specific workout activity the progress
        made towards the specific goal
        Args:
        workout_datafram: dataframe of the workouts of the user
        exercise:type of workout in which you want to achieve the goal. Default is None, to include all types of exercises
        start_time (Date): date at which the goals was set
        end_time (Date): date at which the goals should be reached
        unit_value: specific properties that the user wants to see (kcal,km or min)
        """
        # filter the logWorkout dataframe, containing only all the activities with the same exercise
        # and according to the timeframe
        workout_df = workout_datafram.data
        filtered_workout_dataframe = workout_df[(workout_df['activity'] == exercise) &
                                                      (workout_df['date'] >= start_time) &
                                                      (workout_df['date'] <= end_time)]
        print(filtered_workout_dataframe)
        # convert all distance in standard km? not necessary for the moment
        # create figure
        ax1 = self.fig.add_subplot(self.grid[0,:])
        # create a bar plot according to which type of goal we wants to visualize
        match unit_value:
            case "kcal":
                ax1.bar(
                    filtered_workout_dataframe['date'], filtered_workout_dataframe['calories'], edgecolor='gray')
                ylabel = "Calories"
            case "km":
                ax1.bar(
                    filtered_workout_dataframe['date'], filtered_workout_dataframe['distance'], edgecolor='gray')
                ylabel = "Distance"
            case "min":
                ax1.bar(
                    filtered_workout_dataframe['date'], filtered_workout_dataframe['duration'], edgecolor='gray')
                ylabel = "Duration"
        # add an encouraging message to the plot
        message_index = random.randrange(len(self.messages))
        plt.subplots_adjust(bottom = 0.2)
        plt.gcf().text(0.05, 0.05, self.messages[message_index], fontsize = 12)
        plt.ylabel(ylabel, fontsize=12)
        plt.xticks(rotation=-25, fontsize=8)
        plt.legend(frameon=False)
        plt.title(exercise)
        plt.tight_layout()
        #plt.show()

    def plot_specific_exercise_percentage_terminale(self, dataframe: pd.DataFrame, exercise: str ,unit_value: str, value_goal: float):
        """
        This function plot the a pie chart with the marked workout done towards the goal.
        If the goal has been reached, the pie chart will be color full otherwise only the part
        that has been completed with the percentage
        Args:
        dataframe: the dataframe of the workouts of the user
        unit_value: specific properties that the user wants to see (kcal,km or min)
        value_goal: the goal that the user wants to reach
        """
        # filter the logWorkout dataframe, containing only all the activities with the same exercise
        workout_df = dataframe.data
        # Depending on the unit choosen in the goal dataframe select different column
        unit = self.get_unit(unit_value)
        # Group date according to the unit choosen
        # If there are more workout in one day it will sum the unit according
        progression = workout_df[workout_df['activity'] == exercise].groupby('date')[unit].sum().reset_index()
        print(progression)
        # plot using progress pie chart to shows what is left
        # find th total workout
        total_sum = progression[unit].sum()
        if total_sum >= value_goal:
            # if goal has been reached the pie chart will be complete
            percentage_left = round(total_sum)
            slices = [percentage_left]
            color = ['green']
        else:
            # if the goal has NOT been reached the pie chart wont be completed
            percentage_left = round((total_sum/value_goal)*100)
            slices = [percentage_left,100-percentage_left]
            color = ['green', 'white']
        print(slices)
        print(percentage_left)
        print(value_goal)
        # create figure
        ax3 = self.fig.add_subplot(self.grid[1,:])
        # draw the pie chart
        ax3.pie(slices, colors=color, startangle=90, counterclock=False, normalize=True)
        # add a circle in the middle to draw a donut
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.text(0, 0, f"{percentage_left} %", verticalalignment='center',
                 horizontalalignment='center', fontsize=25, fontname="fantasy")
        plt.title(f"Total Progress {unit.capitalize()}")
        plt.tight_layout()
        plt.show()

    def plot_progression_terminale(self, dataframe: pd.DataFrame, unit_value: str, value_goal: float):
        """
        This function shows the total progression made towards these goal
        Args:
        dataframe: the dataframe of the workouts of the user
        unit_value: specific properties that the user wants to see (kcal,km or min)
        value_goal: the goal that the user wants to reach
        """
        # Depending on the unit choosen in the goal dataframe select different column
        unit = self.get_unit(unit_value)
        # Group date according to the unit choosen
        # If there are more workout in one day it will sum the unit according
        progression = dataframe.data.groupby('date')[unit].sum().reset_index()
        print(progression)
        # create a new column called progress and use the function cumsum
        # that will do partial sum of the row before
        progression['progression'] = progression[unit].cumsum().fillna(
            progression[unit][0])
        
        # create figure
        ax1 = self.fig.add_subplot(self.grid[0,0])
        # draw the bar plot with the progression
        ax1.bar(progression['date'], progression['progression'], color="red")
        # add the label of the partial sum on the top of the bar
        plt.bar_label(plt.bar(
            progression['date'], progression['progression'], color='red'), progression['progression'], fontsize=6)
        # Adjust the ylim to have a 'space' after the goal line : Check that is valid for all the cases
        #plt.ylim(0, value_goal + 100)
        # Draw the horizontal line showing the goal
        ax1.axhline(value_goal, linestyle='--', lw=1.2,
                    color='black', label="Goal", zorder=-1.5)
        # add an encouraging message to the plot
        message_index = random.randrange(len(self.messages))
        plt.subplots_adjust(bottom = 0.2)
        plt.gcf().text(0.05, 0.05, self.messages[message_index], fontsize = 12)
        plt.ylabel(unit.capitalize(), fontsize=8)
        plt.xticks(rotation=25, fontsize=8)
        plt.legend(frameon=False, fontsize=8)
        #plt.show()

    def plot_general_workout_terminale(self, dataframe: pd.DataFrame, unit_value: str):
        """
        This function shows the different types of exercise did every day with different color
        Args:
        dataframe: the dataframe of the workouts of the user
        unit_value: specific properties that the user wants to see (kcal,km or min)
        """
        # Depending on the unit choosen in the goal dataframe select different column
        unit = self.get_unit(unit_value)
        # group each day every sport
        grouped_dataframe = dataframe.data.groupby(
            ['activity', 'date']).sum().reset_index()
        # create a pivot table
        pivot_df = grouped_dataframe.pivot(
            index='date', columns='activity', values=unit)
        print(pivot_df)
        # create figure
        ax2 = self.fig.add_subplot(self.grid[1,:])
        # draw the pivot table
        pivot_df.plot(kind='bar', stacked=True, ax=ax2)
        # Adding labels on top of each bar
        # it adds also the 0, not good!
        # for container in ax.containers:
        #    print(container.pchanged())
        #    print(container.get_label())
        #    ax.bar_label(container, label_type='center')
        # add an encouraging message to the plot
        #message_index = random.randrange(len(self.messages))
        #plt.subplots_adjust(bottom = 0.2)
        #plt.gcf().text(0.05, 0.05, self.messages[message_index], fontsize = 12)
        #plt.xlabel("")
        plt.ylabel(unit.capitalize())
        plt.xticks(rotation=25, fontsize=7)
        plt.legend(title='Activity', frameon=False,loc='upper left', fontsize=8)
        #plt.tight_layout()
        #plt.show()

    def plot_percentage_terminale(self, dataframe: pd.DataFrame, unit_value: str, value_goal: float):
        """
        This function plot the a pie chart with the marked workout done towards the goal.
        If the goal has been reached, the pie chart will be color full otherwise only the part
        that has been completed with the percentage
        Args:
        dataframe: the dataframe of the workouts of the user
        unit_value: specific properties that the user wants to see (kcal,km or min)
        value_goal: the goal that the user wants to reach
        """
        # Depending on the unit choosen in the goal dataframe select different column
        unit = self.get_unit(unit_value)
        # Group date according to the unit choosen
        # If there are more workout in one day it will sum the unit according
        progression = dataframe.data.groupby('date')[unit].sum().reset_index()
        # plot using progress pie chart to shows what is left
        # find th total workout
        total_sum = progression[unit].sum()
        if total_sum >= value_goal:
            # if goal has been reached the pie chart will be complete
            percentage_left = round((total_sum/value_goal)*100)
            slices = [percentage_left]
            color = ['green']
        else:
            # if the goal has NOT been reached the pie chart wont be completed
            percentage_left = round((total_sum/value_goal)*100)
            slices = [percentage_left,100-percentage_left]
            color = ['green', 'white']

        # create figure
        ax3 = self.fig.add_subplot(self.grid[0,1])
        # draw the pie chart
        ax3.pie(slices, colors=color, startangle=90, counterclock=False)
        # add a circle in the middle to draw a donut
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.text(0, 0, f"{percentage_left} %", verticalalignment='center',
                 horizontalalignment='center', fontsize=25, fontname="fantasy")
        plt.title(f"Total Progress {unit.capitalize()}")
        plt.tight_layout()
        plt.show()


class WorkoutSummary:
    """
    Class to plot different summaries on workout data.

    Attributes:
        data: The dataframe of workouts to use as data for the plots.
    """

    def __init__(self, workout_df: WorkoutDataframe):
        self.data = workout_df
        self.fig = plt.figure()
        self.grid = gridspec.GridSpec(3, 3, height_ratios=[1, 1,1])

    def get_timescale(self):
        """
        Prompts the user for the timescale they want to see in the plot.
        """
        while True:
            try:
                timescale = int(input("Over how many of the past days would you like to see the summary? "))
                return timescale
            except ValueError:
                print('Please insert a valid timescale (the number of days as an integer).')

    def get_quantity(self):
        """
        Prompts the user for the workout quantity they want to see in the plot.
        """
        while True:
            quantity = input("Would you like to see the summary for duration, distance or calories? ").lower().strip()
            if quantity in ['duration', 'distance', 'calories']:
                return quantity
            else:
                print("Please select a valid quantity to visualize, either duration, distance or calories.")
    
    def get_exercises(self):
        """
        Retrieves information from the user about which exercises they want to include in the summary.
        """
        entering = "t"
        exercise_list = []
        while entering == "t":
            print(["Running", "Cycling", "Strength", "Swimming", "Walking", "Skiing", "Climbing", "Others"])
            exercise = input(f"Select all exercise you want to include in the summary from the list above, or type q to stop: {exercise_list} ").strip()
            if exercise == "q":
                return exercise_list
            elif exercise.capitalize() in ["Running", "Cycling", "Strength", "Swimming", "Walking", "Skiing", "Climbing", "Others"]:
                exercise_list.append(exercise.capitalize())
            else:
                print("Please enter a valid exercise type. Choose from the list above.")

    def plot_summary(self, timescale: int, quantity: str):
        """
        Plot the duration, distance or calories over time as a stacked bar plot.

        Args:
            timescale: Number of days over which to plot (starting from the date of the most recent workout back).
            quantity: Has to be duration, distance or calories and will be the measure for which the plot is created.
        """
        self.data.data['date'] = pd.to_datetime(self.data.data['date'])
        # first, define the cutoff date from which on you want to do the plot
        latest_date = self.data.data['date'].max()
        print(latest_date)
        cutoff_date = latest_date - pd.Timedelta(days=timescale)

        # select the relevant data from the total of logged workouts
        current_data = self.data.data.loc[self.data.data['date']
                                     >= cutoff_date, ['date', quantity, 'activity']]
        current_data = current_data.pivot(
            index='date', columns='activity', values=quantity)

        # plot
        #choose which suplot to occupy
        ax1 = self.fig.add_subplot(self.grid[0, 0])
        current_data.plot(kind='bar', stacked=True, ax = ax1)
        plt.xlabel('')
        plt.ylabel(quantity)
        plt.xticks(rotation=25)
        plt.legend(title='Activity', frameon=False, fontsize = 8)
        plt.title(label=f'Summary of {quantity} over the last {timescale} days', fontsize = 8)
        plt.tight_layout()
        # plt.savefig("summary.png") save the plot, maybe that will make it easier to work with the GUI
        # plt.close(fig)
        # plt.show() don't show yet, to create the compound figure
    
    def plot_summary_GUI(self, timescale: int, quantity: str):
        """
        Plot the duration, distance or calories over time as a stacked bar plot.

        Args:
            timescale: Number of days over which to plot (starting from the date of the most recent workout back).
            quantity: Has to be duration, distance or calories and will be the measure for which the plot is created.
        """

        # first, define the cutoff date from which on you want to do the plot
        self.data.data['date'] = pd.to_datetime(self.data.data['date'])
        latest_date = self.data.data['date'].max()
        cutoff_date = latest_date - pd.Timedelta(days=timescale)
        print(cutoff_date)
        # select the relevant data from the total of logged workouts
        current_data = self.data.data.loc[self.data.data['date']
                                     >= cutoff_date, ['date', quantity, 'activity']]
        current_data = current_data.pivot(
            index='date', columns='activity', values=quantity)
        print(current_data)
        # plot
        #choose which suplot to occupy
        # create the figure
        fig = Figure(figsize=(5,5), dpi=100)
        ax1 = fig.add_subplot(111)
        current_data.plot(kind='bar', stacked=True, ax = ax1)
        ax1.set_xlabel('')
        ax1.set_ylabel(quantity)
        ax1.tick_params(axis='x',rotation=25)
        ax1.legend(title='Activity', frameon=False, fontsize = 8)
        ax1.set_title(label=f'Summary of {quantity} over the last {timescale} days', fontsize = 8)
        return fig

    def compare_exercises(self, timescale: int, quantity: str, exercises: list):
        """
        Plot the duration, distance or calories compared between two exercises over a specified timescale.

        Args:
            timescale: Number of days over which to plot (starting from the date of the most recent workout back).
            quantity: Has to be duration, distance or calories and will be the measure for which the plot is created.
            exercises: List of exercise types that should be compared.
        """
        # first, define the cutoff date from which on you want to do the plot
        latest_date = self.data.data['date'].max()
        cutoff_date = latest_date - pd.Timedelta(days=timescale)

        # select the relevant data from the total of logged workouts
        current_data = self.data.data.loc[self.data.data['date']
                                     >= cutoff_date, ['date', quantity, 'activity']]
        print(current_data)
        # select only the rows with the activities to compare
        current_data = self.data.data[self.data.data['activity'].isin(exercises)]
        print(current_data)
        # make sure both dataframes have the same format of dates for the concatenation
        current_data['date'] = pd.to_datetime(current_data['date'])
        print(current_data)

        # to get all combinations of date and activity in the dataframe, create a date range and all possible combinations with activities
        dates = pd.date_range(current_data['date'].min(), current_data['date'].max(), freq='1D')

        date_activity_combinations = pd.MultiIndex.from_product(
            [dates, exercises], names=['date', 'activity'])
        all_combinations_df = pd.DataFrame(
            index=date_activity_combinations).reset_index()

        # merge and set the value to 0, if there is no entry for an exercise at any given day
        complete_df = pd.merge(all_combinations_df, current_data, how='left', on=[
                               'date', 'activity'], validate="many_to_many")
        complete_df = complete_df.fillna(0)

        # plot
        ax2 = self.fig.add_subplot(self.grid[0, 1])
        sns.lineplot(data=complete_df, x='date', y=quantity, hue='activity', ax= ax2)
        plt.title(f'Comparison by {quantity} over the last {timescale} days', fontsize = 8)
        plt.xlabel('')
        plt.ylabel(quantity)
        plt.xticks(rotation=25)
        plt.legend(title='Activity', frameon=False, fontsize = 8)
        plt.tight_layout()
        #plt.show()

    def compare_exercises_GUI(self, timescale: int, quantity: str, exercises: list):
        """
        Plot the duration, distance or calories compared between two exercises over a specified timescale.

        Args:
            timescale: Number of days over which to plot (starting from the date of the most recent workout back).
            quantity: Has to be duration, distance or calories and will be the measure for which the plot is created.
            exercises: List of exercise types that should be compared.
        """
        # first, define the cutoff date from which on you want to do the plot
        latest_date = self.data.data['date'].max()
        cutoff_date = latest_date - pd.Timedelta(days=timescale)

        # select the relevant data from the total of logged workouts
        current_data = self.data.data.loc[self.data.data['date']
                                     >= cutoff_date, ['date', quantity, 'activity']]
        print(current_data)
        # select only the rows with the activities to compare
        current_data = self.data.data[self.data.data['activity'].isin(exercises)]
        print(current_data)
        # make sure both dataframes have the same format of dates for the concatenation
        current_data['date'] = pd.to_datetime(current_data['date'])
        print(current_data)

        # to get all combinations of date and activity in the dataframe, create a date range and all possible combinations with activities
        dates = pd.date_range(current_data['date'].min(), current_data['date'].max(), freq='1D')

        date_activity_combinations = pd.MultiIndex.from_product(
            [dates, exercises], names=['date', 'activity'])
        all_combinations_df = pd.DataFrame(
            index=date_activity_combinations).reset_index()

        # merge and set the value to 0, if there is no entry for an exercise at any given day
        complete_df = pd.merge(all_combinations_df, current_data, how='left', on=[
                               'date', 'activity'], validate="many_to_many")
        complete_df = complete_df.fillna(0)

        # plot
        # create the figure
        fig = Figure(figsize=(5,5), dpi=100)
        ax2 = fig.add_subplot(111)
        sns.lineplot(data=complete_df, x='date', y=quantity, hue='activity', ax= ax2)
        ax2.set_title(f'Comparison by {quantity} over the last {timescale} days', fontsize = 8)
        ax2.set_xlabel('')
        ax2.set_ylabel(quantity)
        ax2.tick_params(axis='x', rotation=25)
        ax2.legend(title='Activity', frameon=False, fontsize = 8)
        
        return fig


    def plot_rating_by_exercises(self, timescale: int = None):
        """
        Plot the ratings that were given to the workouts by the type of exercise as Violin plots.

        Args:
            timescale: optional argument to select the number of days over which the plot should be 
            created (back from the date of the most recent workout)."""

        # select the relevant data, if a timescale argument is given
        if timescale is not None:
            latest_date = self.data.data['date'].max()
            cutoff_date = latest_date - pd.Timedelta(days=timescale)
            current_data = self.data.data.loc[self.data.data['date']
                                         >= cutoff_date, ['activity', 'rating']]
        else:
            current_data = self.data.data.loc[:, ['activity', 'rating']]

        # plot
        ax3 = self.fig.add_subplot(self.grid[0, 2])
        sns.violinplot(data=current_data, x="activity",
                       y="rating", inner="point", ax= ax3)
        plt.title(
            'Distribution of Ratings given to workouts of different exercises', fontsize = 8)
        plt.xlabel('')
        plt.ylabel('Rating')
        plt.xticks(rotation=25)
        plt.tight_layout()
        #plt.show()

    def plot_rating_by_exercises_GUI(self, timescale: int = None):
        """
        Plot the ratings that were given to the workouts by the type of exercise as Violin plots.

        Args:
            timescale: optional argument to select the number of days over which the plot should be 
            created (back from the date of the most recent workout)."""

        # select the relevant data, if a timescale argument is given
        if timescale is not None:
            latest_date = self.data.data['date'].max()
            cutoff_date = latest_date - pd.Timedelta(days=timescale)
            current_data = self.data.data.loc[self.data.data['date']
                                         >= cutoff_date, ['activity', 'rating']]
        else:
            current_data = self.data.data.loc[:, ['activity', 'rating']]

        # plot
        # create the figure
        fig = Figure(figsize=(5,5), dpi=100)
        ax3 = fig.add_subplot(111)
        sns.violinplot(data=current_data, x="activity",
                       y="rating", inner="point", ax= ax3)
        ax3.set_title(
            'Distribution of Ratings given to workouts of different exercises', fontsize = 8)
        ax3.set_xlabel('')
        ax3.set_ylabel('Rating')
        ax3.tick_params(axis='x', rotation=25)
        
        return fig

    def plot_pie_sport(self,timescale:int,quantity:str):
        """
        Plot the percentage of every exercises in a pie chart
        Args:
        timescale: optional argument to select the number of days over which the plot should be 
            created (back from the date of the most recent workout)
        quantity: Has to be duration, distance or calories and will be the measure for which the plot is created 
        """
        # first, define the cutoff date from which on you want to do the plot
        latest_date = self.data.data['date'].max()
        cutoff_date = latest_date - pd.Timedelta(days=timescale)

        # select the relevant data from the total of logged workouts
        current_data = self.data.data.loc[self.data.data['date']
                                     >= cutoff_date, ['date', quantity, 'activity']]
        
        coloumn_to_plot = quantity

        aggregate_by_sport = current_data.groupby('activity')[coloumn_to_plot].sum()

        # calulcate percentage
        percentages = (aggregate_by_sport / aggregate_by_sport.sum()) * 100

        # plot
        ax4 = self.fig.add_subplot(self.grid[1,0])

        ax4.pie(percentages, labels=percentages.index, autopct='%1.1f%%', startangle=140)
        plt.title(f'Percentage of Total {coloumn_to_plot.capitalize()} by Activity',fontsize = 8)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        #plt.show()
        #pass

    def plot_pie_sport_GUI(self,timescale:int,quantity:str):
        """
        Plot the percentage of every exercises in a pie chart
        Args:
        timescale: optional argument to select the number of days over which the plot should be 
            created (back from the date of the most recent workout)
        quantity: Has to be duration, distance or calories and will be the measure for which the plot is created 
        """
        # first, define the cutoff date from which on you want to do the plot
        latest_date = self.data.data['date'].max()
        cutoff_date = latest_date - pd.Timedelta(days=timescale)

        # select the relevant data from the total of logged workouts
        current_data = self.data.data.loc[self.data.data['date']
                                     >= cutoff_date, ['date', quantity, 'activity']]
        
        coloumn_to_plot = quantity

        aggregate_by_sport = current_data.groupby('activity')[coloumn_to_plot].sum()

        # calulcate percentage
        percentages = (aggregate_by_sport / aggregate_by_sport.sum()) * 100

        # plot
        # create the figure
        fig = Figure(figsize=(5,5), dpi=100)
        ax4 = fig.add_subplot(111)

        ax4.pie(percentages, labels=percentages.index, autopct='%1.1f%%', startangle=140)
        ax4.set_title(f'Percentage of Total {coloumn_to_plot.capitalize()} by Activity',fontsize = 8)
        ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        return fig

    def scatter_calories_duration(self):

        # Plot the relationship between duration and calories burned
        #plt.figure(figsize=(10, 6))
        ax5 = self.fig.add_subplot(self.grid[1,1])
        sns.scatterplot(data=self.data.data, x='duration', y='calories', hue='activity', style='activity', s=100, ax=ax5)
        plt.title('Relationship Between Duration and Calories Burned',fontsize = 8)
        plt.xlabel('Duration (minutes)')
        plt.ylabel('Calories Burned')
        plt.legend(title='Activity',fontsize = 8, frameon=False)
        #plt.grid(True)
        #plt.show()

    def scatter_calories_duration_GUI(self):

        # Plot the relationship between duration and calories burned
        # create the figure
        fig = Figure(figsize=(5,5), dpi=100)
        ax5 = fig.add_subplot(111)
        sns.scatterplot(data=self.data.data, x='duration', y='calories', hue='activity', style='activity', s=100, ax=ax5)
        ax5.title('Relationship Between Duration and Calories Burned',fontsize = 8)
        ax5.set_xlabel('Duration (minutes)')
        ax5.set_ylabel('Calories Burned')
        ax5.legend(title='Activity',fontsize = 8, frameon=False)

        return fig


    def calories_per_distance(self):

        # Calculate calories burned per kilometer
        self.data.data['calories_per_km'] = self.data.data['calories'] / self.data.data['distance']

        # Plot calories burned per kilometer for each activity
        #plt.figure(figsize=(10, 6))
        ax6 = self.fig.add_subplot(self.grid[1,2])
        sns.barplot(data=self.data.data, x='activity', y='calories_per_km', ax=ax6)
        plt.title('Calories Burned per Kilometer by Activity',fontsize = 8)
        plt.xlabel('Activity')
        plt.ylabel('Calories Burned per Kilometer')
        #plt.grid(True)
        #plt.show()

    def calories_per_distance_GUI(self):

        # Calculate calories burned per kilometer
        self.data.data['calories_per_km'] = self.data.data['calories'] / self.data.data['distance']

        # Plot calories burned per kilometer for each activity
        #plt.figure(figsize=(10, 6))
        fig = Figure(figsize=(5,5), dpi=100)
        ax6 = fig.add_subplot(111)
        sns.barplot(data=self.data.data, x='activity', y='calories_per_km', ax=ax6)
        ax6.set_title('Calories Burned per Kilometer by Activity',fontsize = 8)
        ax6.set_xlabel('Activity')
        ax6.set_ylabel('Calories Burned per Kilometer')
        

        return fig


    def calories_per_duration(self):

        # Calculate caloric efficiency (calories burned per minute)
        self.data.data['caloric_efficiency'] = self.data.data['calories'] / self.data.data['duration']

        # Plot caloric efficiency for each activity
        #plt.figure(figsize=(10, 6))
        ax7 = self.fig.add_subplot(self.grid[2,0])
        sns.barplot(data=self.data.data, x='activity', y='caloric_efficiency', ax=ax7)
        plt.title('Caloric Efficiency by Activity',fontsize = 8)
        plt.xlabel('Activity')
        plt.ylabel('Calories Burned per Minute')
        #plt.grid(True)
        plt.show()

    def calories_per_duration_GUI(self):

        # Calculate caloric efficiency (calories burned per minute)
        self.data.data['caloric_efficiency'] = self.data.data['calories'] / self.data.data['duration']

        # Plot caloric efficiency for each activity
        #plt.figure(figsize=(10, 6))
        fig = Figure(figsize=(5,5), dpi=100)
        ax7 = fig.add_subplot(111)
        sns.barplot(data=self.data.data, x='activity', y='caloric_efficiency', ax=ax7)
        ax7.set_title('Caloric Efficiency by Activity',fontsize = 8)
        ax7.set_xlabel('Activity')
        ax7.set_ylabel('Calories Burned per Minute')
        #plt.grid(True)
        
        return fig

if __name__ == "__main__":

    logWork = pd.DataFrame({'activity': ['Running', 'Cycling', 'Cycling', 'Running', 'Swimming', 'Running'], 'date': [Date(2024, 4, 20).print(), Date(2024, 4, 20).print(), Date(2024, 4, 21).print(), Date(2024, 4, 22).print(), Date(2024, 4, 23).print(), Date(2024, 4, 24).print()], 'duration': [Duration(minutes = 40), Duration(minutes = 80), Duration(minutes = 120), Duration(minutes = 30), Duration(minutes = 20), Duration(minutes = 20)], 'distance': [Distance(9, 'km'), Distance(50, 'km'), Distance(40, 'km'), Distance(6, 'km'), Distance(2, 'km'), Distance(8, 'km')], 'calories': [Calories(200, 'kcal'), Calories(300, 'kcal'), Calories(500, 'km'), Calories(250, 'km'), Calories(400, 'km'), Calories(300, 'km')], 'rating': [Rating(8), Rating(7), Rating(9), Rating(4), Rating(5) , Rating(6)]})

    goalFrame = pd.DataFrame({"value": [300, 100], "unit": ['min', 'km'], "time_scale": [7, 7], "start_date": [Date(2024, 4, 20).print(), Date(2024, 5, 20).print()],
                              "end_date": [Date(2024, 4, 24).print(), Date(2024, 5, 24).print()], "exercise": ['Running', 'Cycling']})

    summary = GoalSummary(logWork, goalFrame)

    # print(summary.plot_goal(7,date.Date(2024,4,20).print(), date.Date(2024,4,24).print(), 'Running', 'Running'))
    summary.plot_goal(0)
    # check the general plotting functions
    workout_summary = WorkoutSummary(logWork)
    workout_summary.plot_summary(2, 'duration')
    workout_summary.compare_exercises(
        10, 'distance', ['Running', 'Swimming', 'Cycling'])
    workout_summary.plot_rating_by_exercises()
