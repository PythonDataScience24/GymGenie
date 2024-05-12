import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from date import Date
from distance import Distance
from duration import Duration
from dataframe import WorkoutDataframe
from calories import Calories
from rating import Rating


class GoalSummary:
    """
    This class retrives the goal for each esercise and plot the current situation, 
    showing what is left

    Attributes:
    log_workout_dataframe: The dataframe of the workouts of the user
    goal_data_frame: The dataframe of the goals of the user
    """

    def __init__(self, log_workout_dataframe: pd.DataFrame, goal_data_frame: pd.DataFrame):
        """
        Initialize a GoalSummary object
        """
        #make the entries for duration, distance, calories and rating numeric
        log_workout_dataframe['duration'] = pd.Series([entry.minutes for entry in log_workout_dataframe['duration']])
        log_workout_dataframe['distance'] = pd.Series([entry.distance_value for entry in log_workout_dataframe['distance']])
        log_workout_dataframe['calories'] = pd.Series([entry.calories_value for entry in log_workout_dataframe['calories']])
        log_workout_dataframe['rating'] = pd.Series([entry.rating_value for entry in log_workout_dataframe['rating']])

        self.log_workout_dataframe = log_workout_dataframe
        self.goal_data_frame = goal_data_frame

    # plot goal using barplot
    def plot_goal(self, index_goal):
        """
        This function shows the plot of the progress through the goal
        Args:
        index_goal: user selection of the goal to plot.
        """

        # plot General goal for week/month/year
        # plot Specific Exercise for week/month/year

        # Checks dataframe objects
        if self.log_workout_dataframe.empty or self.goal_data_frame.empty:
            print(
                'It seems that one of the dataframe has no data. Please add entry before seeing any plot!')
        else:
            # find the value of the goal
            value_goal = float(self.goal_data_frame.iloc[[
                               index_goal]]['value'].item())
            unit_value = self.goal_data_frame.iloc[[
                index_goal]]['unit'].item()
            exercise = self.goal_data_frame.iloc[[
                index_goal]]['exercise'].item()
            start_time = self.goal_data_frame.iloc[[
                index_goal]]['start_date'].item()
            end_time = self.goal_data_frame.iloc[[
                index_goal]]['end_date'].item()
            # DO NOT DELETE YET
            # convert value in standard km, maybe we set up only goals in km
            # if unit_value == "miles":
            #    converted_distance = distance.Distance(value_goal,unit_value)
            #    converted_distance.distance_convert(unit_value, "km")
            #    value_goal = converted_distance.print_distance()

            # Case 1: Specific Exercise
            if type in ["Running", "Cycling", "Strength", "Swimming", 
                        "Walking", "Skiing", "Climbing", "Others"]:

                self.plot_specific_exercise(
                    self.log_workout_dataframe, exercise, start_time, end_time, unit_value)
            else:
                # plot progression
                self.plot_progression(
                    self.log_workout_dataframe, unit_value, value_goal)
                # plot general workout
                self.plot_general_workout(
                    self.log_workout_dataframe, unit_value)
                # plot total workout left to reach the goal
                self.plot_percentage(
                    self.log_workout_dataframe, unit_value, value_goal)

    def plot_specific_exercise(self, workout_datafram: pd.DataFrame, exercise: str, start_time: Date, end_time: Date, unit_value: str):
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
        filtered_workout_dataframe = workout_datafram[(workout_datafram['activity'] == exercise) &
                                                      (workout_datafram['date'] >= start_time) &
                                                      (workout_datafram['date'] <= end_time)]
        print(filtered_workout_dataframe)
        # convert all distance in standard km? not necessary for the moment TODO

        # create a bar plot according to which type of goal we wants to visualize
        match unit_value:
            case "kcal":
                plt.bar(
                    filtered_workout_dataframe['date'], filtered_workout_dataframe['calories'], edgecolor='gray')
                ylabel = "Calories"
            case "km":
                plt.bar(
                    filtered_workout_dataframe['date'], filtered_workout_dataframe['distance'], edgecolor='gray')
                ylabel = "Distance"
            case "min":
                plt.bar(
                    filtered_workout_dataframe['date'], filtered_workout_dataframe['duration'], edgecolor='gray')
                ylabel = "Duration"
        plt.ylabel(ylabel, fontsize=12)
        plt.xticks(rotation=-25, fontsize=8)
        plt.legend(frameon=False)
        plt.title(exercise)
        plt.tight_layout()
        plt.show()

    def plot_progression(self, dataframe: pd.DataFrame, unit_value: str, value_goal: float):
        """
        This function shows the total progression made towards these goal
        Args:
        dataframe: the dataframe of the workouts of the user
        unit_value: specific properties that the user wants to see (kcal,km or min)
        value_goal: the goal that the user wants to reach
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
        progression['progression'] = progression[unit].cumsum().fillna(
            progression[unit][0])
        # draw the bar plot with the progression
        plt.bar(progression['date'], progression['progression'], color="red")
        # add the label of the partial sum on the top of the bar
        plt.bar_label(plt.bar(
            progression['date'], progression['progression'], color='red'), progression['progression'])
        # Adjust the ylim to have a 'space' after the goal line : Check that is valid for all the cases
        plt.ylim(0, value_goal + 50)
        # Draw the horizontal line showing the goal
        plt.axhline(value_goal, linestyle='--', lw=1.2,
                    color='black', label="Goal", zorder=-1.5)
        plt.ylabel(unit.capitalize(), fontsize=12)
        plt.xticks(rotation=25, fontsize=8)
        plt.tight_layout()
        plt.legend(frameon=False)
        plt.show()

    def plot_general_workout(self, dataframe: pd.DataFrame, unit_value: str):
        """
        This function shows the different types of exercise did every day with different color
        Args:
        dataframe: the dataframe of the workouts of the user
        unit_value: specific properties that the user wants to see (kcal,km or min)
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
        grouped_dataframe = dataframe.groupby(
            ['activity', 'date']).sum().reset_index()
        # create a pivot table
        pivot_df = grouped_dataframe.pivot(
            index='date', columns='activity', values=unit)
        print(pivot_df)
        # draw the pivot table
        print(pivot_df.dtypes)
        pivot_df.plot(kind='bar', stacked=True)
        # Adding labels on top of each bar
        # it adds also the 0, not good!
        # for container in ax.containers:
        #    print(container.pchanged())
        #    print(container.get_label())
        #    ax.bar_label(container, label_type='center')
        plt.xlabel("")
        plt.ylabel(unit_value)
        plt.xticks(rotation=25)
        plt.legend(title='Activity', frameon=False)
        plt.tight_layout()
        plt.show()

    def plot_percentage(self, dataframe: pd.DataFrame, unit_value: str, value_goal: float):
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
            slices = [total_sum, round(value_goal-total_sum)]

        # draw the pie chart
        plt.pie(slices, colors=['green'], startangle=90, counterclock=False)
        # add a circle in the middle to draw a donut
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.text(0, 0, f"{percentage_left} %", verticalalignment='center',
                 horizontalalignment='center', fontsize=35, fontname="fantasy")
        plt.title(f"Total Progress {unit.capitalize()}")
        plt.show()


class WorkoutSummary:
    """
    Class to plot different summaries on workout data.

    Attributes:
        data: The dataframe of workouts to use as data for the plots.
    """

    def __init__(self, workout_df: WorkoutDataframe):
        self.data = workout_df

    def get_timescale(self):
        """
        Promps the timescale the user wants to see in the plot
        """
        while True:
            timescale = int(input("Over how many of the past days would you like to see the summary? Select 7/30/365"))
            if timescale in [7,30,365]:
                return timescale
            else:
                print('Please insert a valid timescale.')

    def get_quantity(self):
        """
        Promps the the workout quantity made by the user
        """
        while True:
            quantity = input("Would you like to see the summary for duration, distance or calories? ").lower().strip()
            if quantity in ['duration', 'distance', 'calories']:
                return quantity
            else:
                print("Please select a valid quantity to visualize.")

    def plot_summary(self, timescale: int, quantity: str):
        """
        Plot the duration, distance or calories over time as a stacked bar plot.

        Args:
            timescale: Number of days over which to plot (starting from the date of the most recent workout back).
            quantity: Has to be duration, distance or calories and will be the measure for which the plot is created.
        """

        # first, define the cutoff date from which on you want to do the plot
        latest_date = self.data['date'].max()
        cutoff_date = latest_date - pd.Timedelta(days=timescale)

        # select the relevant data from the total of logged workouts
        current_data = self.data.loc[self.data['date']
                                     >= cutoff_date, ['date', quantity, 'activity']]
        current_data = current_data.pivot(
            index='date', columns='activity', values=quantity)

        # plot
        current_data.plot(kind='bar', stacked=True)
        plt.xlabel('')
        plt.ylabel(quantity)
        plt.xticks(rotation=25)
        plt.legend(title='Activity', frameon=False)
        plt.title(label=f'Summary of {quantity} over the last {timescale} days')
        plt.tight_layout()
        # plt.savefig("summary.png") save the plot, maybe that will make it easier to work with the GUI
        # plt.close(fig)
        plt.show()

    def compare_exercises(self, timescale: int, quantity: str, exercises: list):
        """
        Plot the duration, distance or calories compared between two exercises over a specified timescale.

        Args:
            timescale: Number of days over which to plot (starting from the date of the most recent workout back).
            quantity: Has to be duration, distance or calories and will be the measure for which the plot is created.
            exercises: List of exercise types that should be compared.
        """

        # first, define the cutoff date from which on you want to do the plot
        latest_date = self.data['date'].max()
        cutoff_date = latest_date - pd.Timedelta(days=timescale)

        # select the relevant data from the total of logged workouts
        current_data = self.data.loc[self.data['date']
                                     >= cutoff_date, ['date', 'activity', quantity]]
        # select only the rows with the activities to compare
        current_data = self.data[self.data['activity'].isin(exercises)]

        # to get all combinations of date and activity in the dataframe, create a date range and all possible combinations with activities
        dates = pd.date_range(current_data['date'].min(
        ), current_data['date'].max(), freq='1D')

        # make sure both dataframes have the same format of dates for the concatenation
        current_data['date'] = pd.to_datetime(current_data['date'])

        date_activity_combinations = pd.MultiIndex.from_product(
            [dates, exercises], names=['date', 'activity'])
        all_combinations_df = pd.DataFrame(
            index=date_activity_combinations).reset_index()

        # merge and set the value to 0, if there is no entry for an exercise at any given day
        complete_df = pd.merge(all_combinations_df, current_data, how='left', on=[
                               'date', 'activity'])
        complete_df = complete_df.fillna(0)

        # plot
        sns.lineplot(data=complete_df, x='date', y=quantity, hue='activity')
        plt.title(f'Comparison by {quantity} over the last {timescale} days')
        plt.xlabel('')
        plt.ylabel(quantity)
        plt.xticks(rotation=25)
        plt.legend(title='Activity', frameon=False)
        plt.tight_layout()
        plt.show()

    def plot_rating_by_exercises(self, timescale: int = None):
        """
        Plot the ratings that were given to the workouts by the type of exercise as Violin plots.

        Args:
            timescale: optional argument to select the number of days over which the plot should be 
            created (back from the date of the most recent workout)."""

        # select the relevant data, if a timescale argument is given
        if timescale is not None:
            latest_date = self.data['date'].max()
            cutoff_date = latest_date - pd.Timedelta(days=timescale)
            current_data = self.data.loc[self.data['date']
                                         >= cutoff_date, ['activity', 'rating']]
        else:
            current_data = self.data.loc[:, ['activity', 'rating']]

        # plot
        sns.violinplot(data=current_data, x="activity",
                       y="rating", inner="point")
        plt.title(
            'Distribution of Ratings given to workouts of different exercises')
        plt.xlabel('')
        plt.ylabel('Rating')
        plt.xticks(rotation=25)
        plt.tight_layout()
        plt.show()


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
