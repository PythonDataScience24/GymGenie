import numpy as np


class Distance:
    """
    Represents the distance completed in the exercise.

    Attributes:
        distance (float): The numeric value of the distance.
        unit (str): The unit of measurement ('km', 'm' or 'miles')

    """

    def __init__(self, distance: float, unit: str):
        """
        Initialize a Distance object

        Args:
            distance (float): The numeric value of the distance.
            unit (str): The unit of measurement ('km', 'm' or 'miles')
        """
        self.distance_value = distance
        self.unit = unit.lower()

    def distance_unit_setting(self, unit):
        """
        Set the distance unit.

        Args:
            unit (str): The desired unit ('km', 'm', or 'miles').
        """
        # Validate the unit
        valid_units = ['km', 'm', 'miles']
        if unit.lower() in valid_units:
            self.unit = unit.lower()
        else:
            raise ValueError(f'Invalid unit. Choose from {", ".join(valid_units)}.')

    def distance_convert(self, a, b):
        """
        Convert distance from one unit to another one.

        Args:
            distance (float) : The numeric value of the distance.
            a : current unit.
            b : desired unit to convert to .

        """
        # I am not sure if i should directly modify self.distance
        if a == 'km' and b == 'm':
            self.distance_value = self.distance_value*1000
        elif a == 'm' and b == 'km':
            self.distance_value = self.distance_value/1000
        elif a == 'miles' and b == 'km':
            self.distance_value = self.distance_value*1.60934
        elif a == 'km' and b == 'miles':
            self.distance_value = self.distance_value/1.60934
        elif a == 'm' and b == 'miles':
            self.distance_value = self.distance_value/1609.34
        elif a == 'miles' and b == 'm':
            self.distance_value = self.distance_value*1609.34

        # Round the distance value with 3 decimals
        self.distance_value = round(self.distance_value, 3)
        # Update the unit
        self.unit = b

    def print(self):

        if self.distance_value == np.NAN:
            return np.NAN
        else:
            return f"{self.distance_value} {self.unit}"

    def print_distance(self):
        if self.distance_value == np.NaN:
            return np.NaN
        else:
            return self.distance_value


# Example usage
if __name__ == '__main__':
    my_distance = Distance(distance=10, unit='m')
    print(f"Initial distance: {my_distance.distance_value} {my_distance.unit}")

    # Change the unit to miles
    my_distance.distance_setting('m')
    print(f"Updated distance unit: {my_distance.unit}")

    # Convert from miles to meters
    my_distance.distance_convert('m', 'miles')
    print(f"Converted distance: {my_distance.distance_value} {my_distance.unit}")
