import math
import copy
# written by Mohammad Yasin Karbasian 2023-01-27

class genetic_code:
    # class for saving genetic code properties and other things like the cost to reach this from the initial state
    def __init__(self,current_state,current_cost,heuristic_cost, steps):
        self.current_cost = current_cost
        self.heuristic_cost = heuristic_cost
        self.total_cost = current_cost+heuristic_cost
        self.steps = steps
        self.current_state = current_state

    def __lt__(self, obj):
        return ((self.total_cost) < (obj.total_cost))
  
    def __gt__(self, obj):
        return ((self.total_cost) > (obj.total_cost))
  
    def __le__(self, obj):
        return ((self.total_cost) <= (obj.total_cost))
  
    def __ge__(self, obj):
        return ((self.total_cost) >= (obj.total_cost))
  
    def __eq__(self, obj):
        return (self.total_cost == obj.total_cost)

    def __str__(self):
        return str([self.current_cost, self.heuristic_cost, self.total_cost])

class genetic_path:
    # class for finding the shortest path from the initial state to the wanted state of a genetic code using the A* algorithm

    def __init__(self, array):
        self.initial_state = list(range(1,len(array)+1))
        self.wanted_state = array
        self.explored = list()
        self.frontier = list()

    def heuristic(self,state):
            length = len(state)
            sum = 0
            for i in range(length):
                if state[i] != self.wanted_state[i]: 
                    sum += 1
            return math.ceil(sum/2)

    def solve(self):

        def find_code_one(state):
            for i in range(len(state)):
                if state[i] == 1:
                    return i

        def create_neighbors(gen_code):
            def swap(state, index1, index2):
                state = copy.deepcopy(state)
                temp = state[index1]
                state[index1] = state[index2]
                state[index2] = temp
                return state

            def check(state):
                for i in range(len(self.frontier)):
                    if state == self.frontier[i].current_state:
                        return 0
                for i in range(len(self.explored)):
                    if state == self.explored[i].current_state:
                        return 0
                return 1

            state = gen_code.current_state
            step = gen_code.steps + 1
            cost = gen_code.current_cost + 1
            one_index = find_code_one(state)

            if (one_index+1)%4 == 0:

                if 0 <= one_index+4 <= len(state)-1:
                    new_state = swap(state,one_index,one_index+4)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index-4 <= len(state)-1:
                    new_state = swap(state,one_index,one_index-4)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index-3 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index-3)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index-1 <= len(state)-1:
                    new_state = swap(state,one_index,one_index-1)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

            elif (one_index+1)%4 == 1:

                if 0 <= one_index+4 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index+4)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index-4 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index-4)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index+3 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index+3)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index+1 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index+1)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

            elif (one_index+1)%4 == 2:

                if 0 <= one_index+4 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index+4)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index-4 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index-4)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index+1 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index+1)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index-1 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index-1)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

            elif (one_index+1)%4 == 3:

                if 0 <= one_index+4 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index+4)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index-4 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index-4)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index+1 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index+1)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

                if 0 <= one_index-1 <= len(state)-1:    
                    new_state = swap(state,one_index,one_index-1)
                    if check(new_state):
                        new_code = genetic_code(new_state,cost,self.heuristic(new_state),step)
                        self.frontier.append(new_code)

        estimated_cost = self.heuristic(self.initial_state)
        root = genetic_code(self.initial_state,0,estimated_cost,0)
        self.frontier.append(root)

        while 1:
            if len(self.frontier) == 0:
                return -1
            mini = sorted(self.frontier)[0]
            if mini.current_state == self.wanted_state:
                return mini.steps
            self.frontier.remove(mini)
            self.explored.append(mini)
            create_neighbors(mini)   
            
file = open('./Samples/input_3.txt')
string = file.readlines()

wanted = list(map(int,string[1].strip().split()))
solver = genetic_path(wanted)
print(solver.solve())