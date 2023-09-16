def Robot_Stack_Memoized_Program(robots, ways_b, stacks_n, max_robots_k, stack):
    # memoized condition
    if robots[ways_b][stack] > 0:
        return robots[ways_b][stack]
    # base case
    if(ways_b==0):
        return 1
    # base case 2: if the stack value reaches stacks_n
    if(stack == stacks_n):
        return 0

    # initialize the count to 0
    count = 0
    # for index in range of minimum of ways we can distribute the robots 
    # and max no of robots we can distribute themselves
    for index in range(min(ways_b, max_robots_k)+1):
        
        count += Robot_Stack_Memoized_Program(robots, ways_b-index, stacks_n, max_robots_k, stack+1) 
    
    robots[ways_b][stack] = count
    
    return robots[ways_b][stack]
