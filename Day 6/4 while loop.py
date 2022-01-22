from numpy import number


def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def right_twice():
    turn_right()
    move()
    turn_right()
    

number_of_hurdles = 6
while not at_goal:
    move()
    turn_left()
    move()
    right_twice()
    move()
    turn_left()
    number_of_hurdles -= 1
    print(number_of_hurdles)
    
