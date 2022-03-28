import time
''' 
    alphabet: {0,1}, 0-->"_"; 1-->"1" 
    state: 1,2,3,4,5,"accepte"
    input example: [0]
'''
def five_states_Busy_Beaver(input):
    #initialisation
    current_head = 0
    current_state = 1
    num_step = 0

    while (current_state != "accepte"):
        num_step += 1 
        lire = input[current_head]
        #1-----------------------------------------------
        if (current_state == 1) & (lire == 0) : 
            input[current_head] = 1
            current_head = leftMove(input,current_head)
            current_state = 2
        elif (current_state == 1) & (lire == 1) : 
            input[current_head] = 1
            current_head = rightMove(input,current_head)
            current_state = 3
        #2-----------------------------------------------
        elif (current_state == 2) & (lire == 0) : 
            input[current_head] = 1
            current_head = leftMove(input,current_head)
            current_state = 3
        elif (current_state == 2) & (lire == 1) : 
            input[current_head] = 1
            current_head = leftMove(input,current_head)
            current_state = 2
        #3-----------------------------------------------
        elif (current_state == 3) & (lire == 0) : 
            input[current_head] = 1
            current_head = leftMove(input,current_head)
            current_state = 4
        elif (current_state == 3) & (lire == 1) : 
            input[current_head] = 0
            current_head = rightMove(input,current_head)
            current_state = 5
        #4-----------------------------------------------
        elif (current_state == 4) & (lire == 0) : 
            input[current_head] = 1
            current_head = rightMove(input,current_head)
            current_state = 1
        elif (current_state == 4) & (lire == 1) : 
            input[current_head] = 1
            current_head = rightMove(input,current_head)
            current_state = 4
        #5-----------------------------------------------
        elif (current_state == 5) & (lire == 0) : 
            input[current_head] = 1
            current_head = leftMove(input,current_head)
            current_state = "accepte"
        elif (current_state == 5) & (lire == 1) : 
            input[current_head] = 0
            current_head = rightMove(input,current_head)
            current_state = 1
        # print(input)
    

    print("simulation completed! number of steps is:",num_step)
         

def leftMove(liste,current_head):
    if current_head == 0:
        liste.insert(0,0)
    else:
        current_head -= 1
    return current_head

def rightMove(liste,current_head):
    if current_head >= len(liste) - 1:
        liste.append(0)
    return (current_head + 1)
      
start = time.clock()
five_states_Busy_Beaver([0])
end = time.clock()
print("execution_time: %s seconds"%(end-start))

