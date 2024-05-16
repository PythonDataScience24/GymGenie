class Calories:
    """
    Represents the calories burnt during the exercise.
    
    Atributtes:
        calories (float) : Numeric value
        unit (str) : The unit of measurement ('kcal', 'kJ')
    """
    def __init__(self, calories:int, unit:str) :
        self.calories_value = calories
        self.unit = unit

    def __str__(self):
        return f"{self.calories_value} {self.unit}"

    # I am not sure if this function is useful at all
    def calories_unit_setting(self, unit):
        """
        Set the calories unit.

        Args:
            unit (str): The desired unit ('kcal' or 'kJ').
        """
        #Validate the unit
        valid_units = [ 'kcal', 'kJ']
        if unit in valid_units:
            self.unit = unit
        else:
            raise ValueError(f"Invalid unit. Choose from {', '.join(valid_units)}.")

    def calories_convert(self, a, b):
        """
        Convert calories from one unit to another one.

        Args:
            calories (float) : The numeric value of calories.
            a : current unit.
            b : desired unit to convert to .
        
        """
        #I am not sure if i should directly modify self.distance
        if a == 'kcal' and b == 'kJ':
            self.calories_value = self.calories_value*4.184
            self.unit = 'kJ'
        elif a == 'kJ' and b == 'kcal':
            self.calories_value = self.calories_value/4.184
            self.unit = 'kcal'

        
        #Round the distance value with 3 decimals 
        self.calories_value = round(self.calories_value, 3)
        # Update the unit
        self.unit = b
    def print(self):
        return f"{self.calories_value} {self.unit}"


# Example usage
if __name__ == '__main__':
    my_calories = Calories(calories=10, unit='kJ')
    print(f"Initial calories: {my_calories.calories} {my_calories.unit}")

    # Change the unit to kJ
    my_calories.calories_setting('kcal')
    print(f"Updated calories unit: {my_calories.unit}")

    # Convert from kcal to kJ
    my_calories.calories_convert('kJ', 'kcal')
    print(f"Converted calories: {my_calories.calories} {my_calories.unit}")
