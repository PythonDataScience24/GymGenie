class Rating:
    def __init__(self, rating):
        assert rating >= 1 and rating <= 10, "Rating should be bewtween 1 and 10."
        self.rating = rating