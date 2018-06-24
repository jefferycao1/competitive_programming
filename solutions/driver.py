import time
#import resource
import sys
import math
from collections import OrderedDict

#### SKELETON CODE ####

class queue:
    def __init__(self):
        self.queue = OrderedDict()
        self.configqueue = OrderedDict()
        self.size = 0

    def put(self, item):
        self.queue[item] = 0
        self.configqueue[item.config] = 0
        self.size += 1

    def get(self):
        self.size -= 1
        self.configqueue.popitem(False)[0]
        return self.queue.popitem(False)[0]

    def empty(self):
        return self.size == 0

    def check(self, item):
        if (item.config in self.configqueue):
            return False
        else:
            return True

class PuzzleState(object):

    """docstring for PuzzleState"""

    def __init__(self, config, n, parent=None, action="Initial", cost=0):

        if n*n != len(config) or n < 2:

            raise Exception("the length of config is not correct!")

        self.n = n

        self.cost = cost

        self.parent = parent

        self.action = action

        self.dimension = n

        self.config = config

        self.children = []

        for i, item in enumerate(self.config):

            if item == 0:

                self.blank_row = math.floor(i / self.n)

                self.blank_col = i % self.n

                break

    def display(self):

        for i in range(self.n):

            line = []

            offset = i * self.n

            for j in range(self.n):

                line.append(self.config[offset + j])

            print(line)

    def move_left(self):

        if self.blank_col == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):

        if self.blank_col == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):

        if self.blank_row == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):

        if self.blank_row == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):

        """expand the node"""

        # add child nodes in order of UDLR

        if len(self.children) == 0:

            up_child = self.move_up()

            if up_child is not None:

                self.children.append(up_child)

            down_child = self.move_down()

            if down_child is not None:

                self.children.append(down_child)

            left_child = self.move_left()

            if left_child is not None:

                self.children.append(left_child)

            right_child = self.move_right()

            if right_child is not None:

                self.children.append(right_child)

        return self.children

# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters

def writeOutput(goal_state, cost_of_path, nodes_expanded, max_depth, start_time):
    path = []
    current_state = goal_state
    print("time: %s" %(time.time() - start_time))
    while(current_state.parent is not None):
        path.append(current_state.action)
        current_state = current_state.parent

    path.reverse()

    sys.stdout = open('output.txt', 'wt')


    print("path_to_goal: ", path)
    print("cost_of_path: ", goal_state.cost)
    print("nodes_expanded: ", nodes_expanded)
    print("search_depth: ", goal_state.cost)
    print("max_search_depth: ", max_depth)


    return
    

def bfs_search(initial_state):

    """BFS search"""
    start_time = time.time()
    frontier = queue()
    frontier.put(initial_state)
    current_state = initial_state
    explored = set()
    nodes_expanded = 0
    max_depth = 0

    while(not test_goal(current_state)):
        if(frontier.empty()):
            print("failed")
            return False

        current_state = frontier.get()
        current_state.expand()
        explored.add(current_state.config)

        for child_state in current_state.children:

            if(child_state.config not in explored and (frontier.check(child_state))):
                nodes_expanded += 1

                if(test_goal(child_state)):
                    if(child_state.cost > max_depth):
                        max_depth = child_state.cost
                        writeOutput(child_state, nodes_expanded, nodes_expanded, max_depth, start_time)
                    else:
                        writeOutput(child_state, nodes_expanded, nodes_expanded, max_depth + 1, start_time)
                    return True
                else:
                    frontier.put(child_state)

                if(child_state.cost > max_depth):
                        max_depth = child_state.cost

    if(test_goal(current_state)):
        writeOutput(current_state, nodes_expanded, nodes_expanded, max_depth, start_time)
        return True





def dfs_search(initial_state):

    """DFS search"""
    pass

def A_star_search(initial_state):

    """A * search"""
    pass

def calculate_total_cost(state):

    """calculate the total estimated cost of a state"""
    pass

def calculate_manhattan_dist(idx, value, n):

    """calculatet the manhattan distance of a tile"""
    pass

def test_goal(puzzle_state):

    """test the state is the goal state or not"""
    goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

    if(puzzle_state.config == goal_state):
        return True
    else:
        return False


# Main Function that reads in Input and Runs corresponding Algorithm

def main():
    print("entered")
    sm = sys.argv[1].lower()

    begin_state = sys.argv[2].split(",")

    begin_state = tuple(map(int, begin_state))

    size = int(math.sqrt(len(begin_state)))

    hard_state = PuzzleState(begin_state, size)

    if sm == "bfs":
        bfs_search(hard_state)

    elif sm == "dfs":

        dfs_search(hard_state)

    elif sm == "ast":

        A_star_search(hard_state)

    else:

        print("Enter valid command arguments !")

if __name__ == '__main__':

    main()

