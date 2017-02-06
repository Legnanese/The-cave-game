# This is a first cave
def start():
    print ("You was walking in a gloomy forest in the night")
    print ("Suddenly you see in the dark a cave")
    first_move = raw_input("What is your move?> ")
    if first_move == "enter":
        cave1()
    else:
         print ("You are a bloody chicken!!!!!")

def cave1():
    print ("You have entered in the cave.")

start()
