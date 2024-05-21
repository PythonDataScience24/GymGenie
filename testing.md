# maybe leave out this paragraph
Writing unit tests for our functions was not straightforward at first, because a lot of them don't directly return something, but rather modify the data in place or create some plots. As a naive way of testing, we included some code to try out the functions at the bottom of most modules.
For the unit testing, we chose some functions, to start at a small scale.

# Test the function Distance.distance_convert()
To test this function, we used a glass-box approach, where we looked at all the possible paths we can take through this function, with the different conversions between combinations of km, m and miles. However, we might miss some boundary cases with this approach, for example when the input to the function is of an unexpected format or type


# Other ideas for functions to test:
Distance.distance_unit_setting(), which can raise an exception
Duration.short_str()
Dataframe.extract_date() and the other extract functions
maybe the column names when creating a Workout or Goal Dataframe?