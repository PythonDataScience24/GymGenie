import sys

# start the program
if __name__ == "__main__":
    program = True
    print("Hey, welcome to GymGenie!")
    print("What do you want to do?")
    while program:       
        # choose a command
        try:
            option = input("Choose:\n 1.Statistics\n 2.Add Workouts\n 3.Add Goal\n 4.Visualize Trends\n")

            if(int(option) == 1):
                print("A")
                # insert code from kristin&Laura
            elif(int(option) == 2):
                print("B")
                # insert code from kristin&Laura
            elif(int(option) == 3):
                print("C")
                # insert code from kristin&Laura
            elif(int(option) == 4):
                print("D")
                # insert code from kristin&Laura
            else:
                program = False
                sys.exit("GymGenie has been terminated")
        except ValueError:
            print("Wrong format. Please use only integers!")
        
