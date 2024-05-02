## Documentation


### Python Environment
To start our program you need to have installed python. We suggested to use *Anaconda*, an open-source package and environment management system that runs on Windows, macOS, and Linux. For more information click [here](https://docs.anaconda.com/free/anaconda/install/index.html).

After you installed *Anaconda* you can create a environment. In the terminal type the following command:
<pre> conda create --name my-env </pre>

In this way, you created your own environment. To activate your environment you can type:

<pre> conda activate my-env</pre>

When you have activated you environment, goes in the folder of the repository and type the following command:
<pre> pip install -r requirements.txt </pre>

After that all the necessary packages will be installed in your environment.

### Start the Programm
Go in the folder of the repository and type the following command:
<pre> python .\src\main.py </pre>
If you are using MacOS or Linux the path of the file has to be adjusted.

After starting the program it will appear the menu page of our program.
![alt text](image.png)

Have fun exploring our program.

### Functionality

In the menu of the program if you type *w*, it will appear the window to insert a workout. Instead if you type *g*, you will able to set up a goal according to your preferences. Typing *o*, you will check how much progress did you made towards your goal. Then typing *s*, you will see the summary of your workouts filtered by exercise, by the timeframe, ect. Finally, typing *q* you will exit the program.
