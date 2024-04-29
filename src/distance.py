import numpy as np
class Distance:
    """
    Represents the distance completed in the exercise.

    Attributes:
        distance (float): The numeric value of the distance.
        unit (str): The unit of measurement ('km', 'm' or 'miles')
    
    """
    def __init__(self, distance, unit):
        """
        Initialize a Distance object

        Args:
            distance (float): The numeric value of the distance.
            unit (str): The unit of measurement ('km', 'm' or 'miles')
        """
        self.distance = distance
        self.unit = unit.lower()
    
    # I am not sure if this function is useful at all
    def distance_setting(self, unit):
        """
        Set the distance unit.

        Args:
            unit (str): The desired unit ('km', 'm', or 'miles').
        """
        #Validate the unit
        valid_units = [ 'km', 'm', 'miles']
        if unit.lower() in valid_units:
            self.unit = unit.lower()
        else:
            raise ValueError(f"Invalid unit. Choose from {', '.join(valid_units)}.")

    def distance_convert(self, a, b):
        """
        Convert distance from one unit to another one.

        Args:
            distance (float) : The numeric value of the distance.
            a : current unit.
            b : desired unit to convert to .
        
        """
        #I am not sure if i should directly modify self.distance
        if a == 'km' and b == 'm':
            self.distance = self.distance*1000
        elif a == 'm' and b == 'km':
            self.distance = self.distance/1000
        elif a == 'miles' and b == 'km':
            self.distance = self.distance*1.60934 
        elif a == 'km' and b == 'miles':
            self.distance = self.distance/1.60934 
        elif a == 'm' and b == 'miles':
            self.distance = self.distance/1609.34 
        elif a == 'miles' and b == 'm':
            self.distance = self.distance*1609.34 
        
        #Round the distance value with 3 decimals 
        self.distance = round(self.distance, 3)
        # Update the unit
        self.unit = b
    def print(self):

        if self.distance == np.NAN:
            return np.NAN
        else:
            return f"{self.distance} {self.unit}"

        
        
# Example usage
if __name__ == '__main__':
    my_distance = Distance(distance=10, unit='m')
    print(f"Initial distance: {my_distance.distance} {my_distance.unit}")

    # Change the unit to miles
    my_distance.distance_setting('m')
    print(f"Updated distance unit: {my_distance.unit}")

    # Convert from miles to meters
    my_distance.distance_convert('m', 'miles')
    print(f"Converted distance: {my_distance.distance} {my_distance.unit}")








    
    
