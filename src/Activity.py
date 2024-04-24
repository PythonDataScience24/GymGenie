class Exercise:
    def __init__(self, exercise_type):
        self.exercise_type = exercise_type

    def select_type(self):
        selected_type = input("Select type of exercise: running, cycling, ")
        self.exercise_type = selected_type