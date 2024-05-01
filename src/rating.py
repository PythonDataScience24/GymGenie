class Rating:
    """
    A rating of how a workout felt like.

    Attributes:
        rating (int) : Rating of the workout (from 1 to 10)
    """
    def __init__(self, rating):
        self.rating = rating
    
    def print(self):
        return self.rating