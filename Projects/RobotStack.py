import sys

def Robot_Stack_Memoized_Program(robots, ways_b, stacks_n, max_robots_k, stack):
    # memoized condition
    # if robots[ways_b][stack] > 0:
    #     return robots[ways_b][stack]
    # base case
    if(ways_b==0):
        return 1
    # base case 2: if the stack value reaches stacks_n
    if(stack == stacks_n):
        return 0

    # initialize the count to 0
    c_robots = 0
    # for index in range of minimum of ways we can distribute the robots 
    # and max no of robots we can distribute themselves
    for index in range(min(ways_b, max_robots_k)+1):
        # print("Entered For loop")
        c_robots = c_robots + Robot_Stack_Memoized_Program(robots, ways_b-index, stacks_n, max_robots_k, stack+1) 
    
    robots[ways_b][stack] = c_robots
    
    return robots[ways_b][stack]

# ways_b,stacks_n,max_robots_k = 3,4,2
# memo = [[-1 for _ in range(stacks_n+1)] for _ in range(ways_b+1)]
# print(roboStack(memo, ways_b,stacks_n,max_robots_k, 0))
with open(sys.argv[1], 'r') as input_file:
    # to get the values of the input line by line
    for i_f in input_file:
        # split the inputs
        ways_b,stacks_n,max_robots_k = i_f.split(' ')
        # type cast the inputs
        ways_b = int(ways_b)
        stacks_n = int(stacks_n)
        max_robots_k = int(max_robots_k)
        # initalize how many robots we can traverse to -1, by default.
        robots = [[-1 for _ in range(stacks_n+1)] for _ in range(ways_b+1)]
        # call the function that does the job
        rs = Robot_Stack_Memoized_Program(robots, ways_b, stacks_n, max_robots_k, 0)
        # finally print the outputs
        print("({0},{1},{2}) = {3}".format(ways_b,stacks_n,int(max_robots_k), rs))
