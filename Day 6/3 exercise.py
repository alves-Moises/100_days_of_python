def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def right_twice():
    turn_right()
    move()
    turn_right()
    
for i in range(6):
    move()
    turn_left()
    move()
    right_twice()
    move()
    turn_left()
    
