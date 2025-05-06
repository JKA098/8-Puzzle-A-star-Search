# the time module is for measuring time taken
import time


"""this module is for getting information on the system 
    and resources; that way we can get peak memory usage, 
    and the number of nodes generated """
import psutil


"""this allows to create combinations. 
    One case use is when a higher number 
    tile precedes a lower number tile,
    if there is the need for these number to be combined
    in a given logic; largest to smallest, the combinations 
    module is of great help"""
from itertools import combinations


""" this code import a module that provides 
        default values. More specifically, 
        it allow to initialize default values 
        for a grid or game board, 
        like the one found in the 8-puzzle tile."""
from collections import defaultdict


"""this module implements a heap queue or priority 
        queue. Which makes for good data structure 
        that the algorithm can 
        use to efficiently retrieve the smallest 
        or largest number, which allows for numbers to
        be stored in a sorted fashion"""
import heapq

# this module allows us to generate random numbers.
import random



# Abstract Problem class
"""this code is for crating the class Problem, 
    which is basically just a set of instructions. 
    And for this code there are functions that define
    the actions, result, goals, path cost and different
    heuristics that will be defined further down"""
class Problem:
    def __init__(self, initial=None, goal=None, **kwds):
        # this is define the initial state of the class.
        """ **kwds: is for an additional keyword, 
            or argument that will be added to the class, 
            of the defined function. That way, 
            there is no need to have to go back and add changes."""

        """initial and goal, are part of what will be 
            used in the creation of the algorithm and are set to 
            none since they are not known yet"""

        self.__dict__.update(
            initial=initial, 
            goal=goal, **kwds)
        # the above code allow for updating the initial and goal values

    """this will define the action that 
        will be taken. And the returned 
        value is just an abstract method, 
        that can be used to remind yourself to 
        implement the method correctly"""
    def actions(self, state):
        raise NotImplementedError

    # this will define the result that will be received. 
    def result(self, state, action):
        raise NotImplementedError

    # this function, more or less, check if the state, matches the goal
    def is_goal(self, state):
        return state == self.goal
    
    # this function return the cost associated with performing an action “a”. In this case going from s to s1
    def action_cost(self, s, a, s1):
        return 1

    # this function represent a heuristic with a default value of 0 
    # unless otherwise specified, and has for argument self and node
    def h(self, node):
        return 0

# Node class
"""this class is for defining the element of a Node. 
        Nodes are important in search algorithms, 
        as they help in representing and managing the search process. 
        They basically give the current state, and the state that
        comes after generating a node"""
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        # this represents the current state
        self.state = state

        # this represents the parent state, which is the preceding step/stage
        self.parent = parent

        # this represents the action taken, which let us know the difference action taken to get to a current step/stage.
        self.action = action

        # this represents the cost to reach a given step/stage
        self.path_cost = path_cost

    """this function “_lt_” stands for “less than”, 
        and is use for comparison purposes. 
        It is particularly useful for priority queue, 
        whereby there is comparison to see which path 
        has higher priority, and by extension, 
        which nodes should have higher priority."""
    def __lt__(self, other):
        return self.path_cost < other.path_cost

# Priority Queue
class PriorityQueue:
    """this funciton defines the initial arguments and 
        their corresponding values. In this case 
        it defines the initial arguments of the priority queue."""
    def __init__(self, items=(), key=lambda x: x):
        # key is the part that determines the priority for each item
        self.key = key
        self.items = []
        for item in items:
            self.add(item)

    """this define how elements are added. 
        And using the “.heappush” method, 
        items are added based on their priority"""
    def add(self, item):
        heapq.heappush(self.items, (self.key(item), item))

    # this define how elements are removed
    def pop(self):
        return heapq.heappop(self.items)[1]

    # this returns the number of items in the priority queue
    def __len__(self):
        return len(self.items)


# Expand function
""" more or less this function does the expansion. 
        Basically, it creates from the current node, 
        all possible successor nodes.
        then create a for loop, look at the 
        actions of a given state and then generate 
        a new state and each state is 
        wrapped in a Node object with corresponding, 
        parent node and path cost"""
def expand(problem, node):
    # this code extracts a state from the given node
    state = node.state

    # this for loop, loops over all possible actions from the given state
    for action in problem.actions(state):

        # this the resulting state
        new_state = problem.result(state, action)

        # this code update the path cost based on action cost
        cost = node.path_cost + problem.action_cost(state, action, new_state)
        
        # this code return the new node with the new state, and return the path cost
        yield Node(new_state, node, action, cost)

# 8-puzzle problem
class EightPuzzle(Problem):
    """this part, gives the arguments and stores 
        the initial and goal state as a tuple
        in here, the initial value can be 
        any version, but the goal state is defined.
        the zero, represents the blank title"""

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        self.initial = tuple(initial)
        self.goal = tuple(goal)

    # this function, is for defining the moves that are acceptable
    def actions(self, state):

        # these are all the possible moves 
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # this define the code that finds the blank 
        # tile in a 1D tuple representation of the board
        blank = state.index(0)

        # this convert the index that is in 1D position
        #  into another made of 
        # rows and columns that is in a 2D positions
        row, col = divmod(blank, 3)

        # this create an empty list that will store the valid moves
        valid_moves = []

        """this is a for loop, that go through all 
            the moves and check which moves are valid.
            dr and dc stands respectively for delta row
            and column. And represents how much to 
            change the row/column index when moving a tile"""
        for dr, dc in moves:
            # this code computes the new move
            r, c = row + dr, col + dc

            # this code checks that the new move is within 
            # a specified bound. If it is, it gets added 
            # to the empty valid_moves list created above.
            if 0 <= r < 3 and 0 <= c < 3:
                valid_moves.append((r * 3 + c))
        return valid_moves

    # this function returns the new state 
    # that is created, after moving the blank tile, 
    # and has 2 parameters state and action.
    def result(self, state, action):
        # this code find the actual blank/empty tile
        blank = state.index(0)

        # this code turns the state obtained into a list
        state = list(state)

        # this code swaps blank state tile with the action tile
        state[blank], state[action] = state[action], state[blank]
        
        # this convert the previous state that was 
        # stored into a list, 
        # to a being stored as a tuple,
        # and return it
        return tuple(state)


    # this the beginning of the heuristic function, 
    # and define how h1 is. It takes a node as parameter
    # and compares its state with the goal state
    def h1(self, node):

        # this code, more or less count and 
        # return the number of tiles that are in the 
        # wrong position, excluding blank tile.
        return sum(1 for s, g in zip(node.state, self.goal) if s != g and s != 0)

    
    # this define the function h2 which 
    # calculates the Manhattan distance heuristic.
    def h2(self, node):

        """Manhattan heuristic calculation."""

        # this is code initialise the state object. 
        # Which will hold the 
        # arrangement of tiles in the puzzle.
        state = node.state

        """this code creates a sort of look up dictionary, 
           that allows to map each tile value to its row 
           and column in the goal state
           
           (i // 3, i % 3)) represents the Row and 
           column position of each tile in the goal state,
           which allows to know where each tile is in the puzzle
           and by extension where it is suppose to be """
        
        goal_positions = {val: (i // 3, i % 3) for i, val in enumerate(self.goal)}  
        

        """ the following code, especially the part in sum() 
                uses a specific formula, that in the end, 
                it gives the total Manhattan distance"""

        """ in addition, it loops through each 
                tile position and value in 
                “state” and skips the blank tile 0."""

        """furthermore it extracts the current position 
                  of the tile, while also converting the 
                  initial 1D index( either list or tuple) 
                  into a 2D index with coordinates 
                  and respective row and column index."""
        return sum(abs(row - goal_positions[val][0]) + abs(col - goal_positions[val][1])
                # for this code, it loops through each 
                # tile’s position and value in 
                # “state” and skips the blank tile 0.
                for i, val in enumerate(state) if val != 0 
                for row, col in [(i // 3, i % 3)])  


    # this code returns h3, which is the max of h1 and h2
    def h3(self, node):
        return max(self.h1(node), self.h2(node))

    # this code returns h3, which is the max of h1, h2 and h3
    def h4(self, node):
        return max(self.h1(node), self.h2(node), self.h3(node))


# A* search algorithm

"""this part of the code defines the astar_search function with two 
        parameters problem and heuristic, which are 
        inherited from the previous function 
        created or codes written."""
def astar_search(problem, heuristic):

    # this code create a variable, 
    # that represent the initial 
    # state of the problem
    start_node = Node(problem.initial)


    """this code initialise the priority queue.
            here lambda calculate the cost for each node, 
            and those with a lower cost, are prioritized"""
    frontier = PriorityQueue([start_node], key=lambda n: n.path_cost + heuristic(n))
    

    # this code initialize the explored variable, 
        # which will store already visited states, 
        # and potentially avoid loops
    explored = set()


    # this code will be used to count the number of nodes 
        # that have been created, and will be 
        # necessary for performance measurement
    nodes_generated = 0


    # this the beginning of a while for loop,
    # which excecute given certain conditions
    while frontier:

        """this code retrieves the node with the 
            favorable path based cost, 
            as calculated by the “PriorityQueue” """
        node = frontier.pop()

        # this code checks if the current node 
        # is the desired node, as stated by the goal node, 
        # then return it.
        if problem.is_goal(node.state):
            return node, nodes_generated
        
        # this add the node’s state to explored, 
        # that way it does not get revisited again
        explored.add(node.state)


        # this is a for loop. Which is used to 
        # generate new nodes: child notes
        for child in expand(problem, node):

            # this how the extra nodes(child nodes) are 
                # generated. Which can also used to 
                # track or count the number of nodes created
            nodes_generated += 1

            # this code, checks for the new node/child state, 
                # if it has already been explored/visited, it is 
                # added to the priority queue. 
                # This has the added benefit of not 
                # revisiting the old states unnecessarily.
            if child.state not in explored:
                frontier.add(child)

    """this code returns None, in the case there 
        are no state that have not been visited, 
        and return the number of nodes
        (child node/state) that have been generated."""
    return None, nodes_generated

# Measure memory usage

"""this function has for sole purpose 
        measuring the memory usage and 
        returns the output in megabutes(MB)"""
def memory_usage():

    """this where the psutil module imported comes in handy.
        the first step is to create an object that 
        represents the running python process
        due to the fact that psutil module is a 
        system utility module, it can provide access 
        to system-related information, 
        such as CPU usage, memory usage and running process."""
    process = psutil.Process()

    """this the code that converts the obtained result 
        into a readable format such as converting bytes to MB
    here “process.memory_info()” retrieves detailed 
        memory related to usage statistics
        and “.rss” (Resident Set Size) returns the 
        actual physical memory (RAM) being used 
        by the process.
    “/(1024 ** 2)” converts the memory usage 
        from bytes to megabytes (MB)."""
    return process.memory_info().rss / (1024 ** 2)  # Convert to MB

# Main program
"""this is the main function program. 
    It does not take any parameters, 
    since it will collects input as it goes"""
def main():
    # Input or random generation
    """ this initialise the initial input. 
            In this case, the user is asked to input 
            an given initial configuration or 
            press enter to randomize"""
    initial = input("Enter initial configuration as 9 space-separated numbers (or press Enter to randomize): ")
    
    """ this code specifies what happens 
            in the event that no input is given, 
            and specify that a random puzzle is generated"""
    if not initial:
        initial = list(range(9))
        
        # this code shuffle the provided list above
        random.shuffle(initial)
    
    # this code specifies what happen 
    # in the event an input is given. 
    else:
        
        # here the initial.split(), splits 
            # the input into a list of string numbers
            # then convert the strings to an integer
        initial = list(map(int, initial.split()))

    # this code display the initial puzzle state 
    print("\nInitial State:")
    print(f"{initial[:3]}\n{initial[3:6]}\n{initial[6:]}")


    # this code create an instance of 
    # EightPuzzle given the “initial” state
    puzzle = EightPuzzle(initial)

    # this part is for calculating the 
    # different heuristics value 
    # and printing them
    initial_node = Node(puzzle.initial)
    h1_val = puzzle.h1(initial_node)
    h2_val = puzzle.h2(initial_node)
    h3_val = puzzle.h3(initial_node)
    h4_val = puzzle.h4(initial_node)
    print("\nInitial Heuristic Values:")
    print(f"h1: {h1_val}, h2: {h2_val}, h3: {h3_val}, h4: {h4_val}")


    # this initialise a dictionary for the measured metrics
    metrics = {}

    # this code runs a for loop through the 
        # four heuristic created above, while 
        # keeping track of the heuristic index. 
        # and print the result
    for i, heuristic in enumerate([puzzle.h1, puzzle.h2, puzzle.h3, puzzle.h4], start=1):
        print(f"\nRunning A* with h{i}...")


        # this records the start time, and measured 
            # memory usage all 
            # which are useful metric before A search.
        start_time = time.time()
        start_memory = memory_usage()


        # this calls the A* search algorithm
        solution, nodes_generated = astar_search(puzzle, heuristic)
        
        
        # this records the end time, and 
            # measured memory usage all which 
            # are useful metric after A search.
        end_time = time.time()
        end_memory = memory_usage()


        # this code stores the result for time, 
            # memory and nodes generated into 
            # the metrics dictionary created above.
        metrics[f"h{i}"] = {
            "time": end_time - start_time,
            "memory": end_memory - start_memory,
            "nodes_generated": nodes_generated
        }

    # the for loops below iterate through the ‘metrics.item’, 
        # to display execution time, 
        # memory usage and total nodes generated.
    print("\nPerformance Metrics:")
    for h, m in metrics.items():
        print(f"{h}: Time = {m['time']:.4f}s, Memory = {m['memory']:.2f} MB, Nodes Generated = {m['nodes_generated']}")


# this will ensure the main() function 
    # created above, only runs when the code is executed 
    # directly and not when imported as a module.
if __name__ == "__main__":
    main()

