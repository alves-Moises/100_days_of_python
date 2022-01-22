def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def right_twice():
    turn_right()
    move()
    turn_right()
    

while not at_goal():
    if front_is_clear():
        move()
        if right_is_clear():
            turn_right()
      
    else:
        while not front_is_clear():
            turn_left()
            
            

  