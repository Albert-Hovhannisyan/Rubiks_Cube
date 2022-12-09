from queue import LifoQueue, PriorityQueue
from Cube import Cube, perform
from Manhatten import Manhatten
import time

correct = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
rotation = ['R7', 'R4', 'G1', 'R8', 'R5', 'G2', 'R9', 'R6', 'G3', 'B1', 'B2', 'B3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'Y7', 'Y4', 'Y1', 'Y8', 'Y5', 'Y2', 'B9', 'B6', 'R3', 'G7', 'G4', 'O1', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'Y9', 'O2', 'O3', 'Y6', 'G5', 'G6', 'Y3', 'G8', 'G9', 'R1', 'R2', 'W1', 'B4', 'B5', 'W2', 'B7', 'B8', 'W3']
move_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def idastar(scramble):
    
#have a priority queue "f_values" with the f of frontier nodes
    stack = LifoQueue()
#have a list of lists where we have the array, the g, the h, and the f (for both in and out of limit nodes)
#have a priority queue for the f values above the limit "above_limit"
    above_limit = PriorityQueue()
#have a variable "g" with the g value of the node being expanded
    g = 0
#have a variable "current_g"
    x = Manhatten(scramble)
    limit = x

    current_h = x
    current_g = 0
    current_f = x
    
    found = False

    iterations = 0

    if correct == scramble:
        return correct
    else:
        start = time.time()
        while current_g < 20:
            stack.put([scramble, 0, x, x])
            while stack.empty() == False:
                parent = stack.get()
                parent_g = parent[1]
                for j in move_list:
                    tmp = Cube(parent[0])
                    perform(tmp, j)
                    child = tmp.get_state()
                    # print(child)
                    if correct == child:
                        found = True
                        end = time.time()
                        print("Found solution")
                        print(end - start)
                        print("Itaeration", iterations)
                        # print(child)
                        return found
                    current_h = Manhatten(child)
                    current_g = parent_g+1
                    current_f = current_g + current_h
                    # print(current_f)
                    # print(limit)
                    if current_f <= limit:
                        stack.put([child, current_g, current_h, current_f])
                    else:
                        above_limit.put(current_f)
            limit = above_limit.get()
            stack.queue.clear()
            print(iterations)
            print("New Limit", limit)
            iterations += 1
            above_limit.queue.clear()
        end = time.time()
        print(end - start)
        print("No")
        return False


trial = ['Y7', 'G2', 'O9', 'R8', 'R5', 'O8', 'R9', 'R6', 'Y3', 'R3', 'B2', 'W1', 'R2', 'O5', 'O2', 'W9', 'O6', 'O3', 'B9', 'Y4', 'G1', 'B6', 'Y5', 'W6', 'B3', 'Y6', 'B7', 'G7', 'G4', 'G3', 'W4', 'W5', 'G6', 'B1', 'B4', 'G9', 'W7', 'G8', 'Y9', 'W8', 'G5', 'Y8', 'O1', 'O4', 'O7', 'R7', 'R4', 'R1', 'Y2', 'B5', 'W2', 'Y1', 'B8', 'W3']
one = ['B1', 'B2', 'B3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'G1', 'G2', 'G3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'Y3', 'Y6', 'Y9', 'Y2', 'Y5', 'Y8', 'Y1', 'Y4', 'Y7', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'R1', 'R2', 'R3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'O1', 'O2', 'O3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']
two = ['R7', 'R4', 'R1', 'R8', 'R5', 'R2', 'R9', 'R6', 'R3', 'O7', 'O4', 'O1', 'O8', 'O5', 'O2', 'O9', 'O6', 'O3', 'G3', 'G6', 'G9', 'Y4', 'Y5', 'Y6', 'B9', 'B6', 'B3', 'G7', 'G4', 'G1', 'W4', 'W5', 'W6', 'B1', 'B4', 'B7', 'Y7', 'G2', 'W9', 'Y8', 'G5', 'W8', 'Y9', 'G8', 'W7', 'Y3', 'B2', 'W1', 'Y2', 'B5', 'W2', 'Y1', 'B8', 'W3']
tree = ['Y7', 'G2', 'W9', 'R8', 'R5', 'R2', 'R9', 'R6', 'R3', 'Y3', 'B2', 'W1', 'O8', 'O5', 'O2', 'O9', 'O6', 'O3', 'B9', 'Y4', 'G3', 'B6', 'Y5', 'G6', 'B3', 'Y6', 'G9', 'G7', 'G4', 'G1', 'W4', 'W5', 'W6', 'B1', 'B4', 'B7', 'O7', 'O4', 'O1', 'Y8', 'G5', 'W8', 'Y9', 'G8', 'W7', 'R7', 'R4', 'R1', 'Y2', 'B5', 'W2', 'Y1', 'B8', 'W3']


# result = idastar(tree)
# print(result)