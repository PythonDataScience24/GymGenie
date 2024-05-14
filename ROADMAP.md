## Project Roadmap

Welcome to the Roadmap of the fitness tracking application GymGenie. Here you can learn what this project is about, how to get involved, and which stages the development of our project includes.
We are four Bioinformatics students developing the application. Our application is targeted to anyone who wants to simplify the process of tracking workouts and analysing the progress. With features for setting goals and visualising the progress towards them, we want to make it easier for users to be consistent in their workout schedule and to reach their goals.

If you want to get involved as a contributor, we are happy to learn your suggestions for features our application should include. Or, once the project has developped a bit more, contributors can help by testing the application or proof-reading our code.  Feel free to reach out and send us an e-mail with your suggestions (laura.fernandez@students.unibe.ch, kristin.olsen@students.unibe.ch, dario.bassi@students.unibe.ch, lea.frei@students.unibe.ch).

## Timeline:

### Milestone 1: Exercise Logging
Allow users to input data about their workouts, including the type of exercise, duration, distance (if applicable), and calories burned. Store this data in a dataframe.
- **Deadline**: 02.05.2024

### Milestone 2: Goal Setting and Progress Tracking
Enable users to set personal fitness goals, such as weekly exercise duration, distance, or calories burned. Retrieve and display their progress toward these goals based on their logged workouts.
- **Deadline**: 16.05.2024

### Milestone 3: Data Visualization and Trends
Provide users with visualizations of their exercise data, such as weekly/monthly summaries, progress charts, or comparisons of different exercise types. Allow users to analyze trends in their workout habits over time.
- **Deadline**: 23.05.2024

## Tasks to be done for each milestone:

### Milestone 1:

- Create the parent class `Workout` with the properties: date, duration, calories, distance, and rating.
- Create eight child classes `Running`, `Cycling`, `Strength`, `Swimming`,`Skiing`, `Walking`, `Climbing` and `Other` that represent the type of activity.
- Include subclasses that represent the properties for each activity:
    - `Date`: Date of the workout
    - `Duration`: Duration of the workout in minutes
    - `Calories`: Calories burned during the workout
    - `Distance`: Distance covered during the workout (if applicable)
    - `Dataframe`: Pandas dataframe to store workout data. 
                  It is written in a csv file. When the user close the session the data is saved and then when it re-opens, we can read and re-use it.
    - `Rating`: Rating of the workout on a scale of 1 to 10
- **Contributors**: Laura, Kristin
- Create `main.py` to run the main program 
- Implement user interaction for inputting workout data sequentially
  - Show summary and allow user for modification or saving at the end
- - **Contributors**: Lea, Dario
- Open for future or to other contributors: suggest calories in-take
- Open for contributors: testing with MAC operating system


### Milestone 2:
- Create `Goals` class for setting and managing fitness goals
  - Allow setting goals for duration, distance, or calories burned 
  - Provide tips for SMART goals
  - Specify the timeframe (week/month/year)
- Implement `Progress` class for tracking progress toward goals
  - Plot progress( in terms of duration/calories/distance) over time 
  - Provide feedback (a goal is reached / "keep going" / not reached yet) on goal achievement
  - Develop the GUI
- **Contributors**: Laura, Kristin, Lea, Dario

### Milestone 3:
- Develop `Summary` class to generate summaries and visualizations of exercise data
  - Merge different types of exercises (e.g. running and cycling), show weekly and monthly trends
  - Show specific behaviour in the exercises
  - Perform linear regression of general exercise and specific sports
  - Comparison of different exercises
- **Contributors**: Laura, Kristin, Lea, Dario

## Relevant timeframes:
30.05.2024 - End subtasks and write documentation





