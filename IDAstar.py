from queue import LifoQueue, PriorityQueue
from Cube import Cube, perform
from ManhattenIDAstar import ManhattenIDAstar
import time

correct = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
move_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def IDAstar(scramble):
    stack = LifoQueue()
    above_limit = PriorityQueue()

    x = ManhattenIDAstar(scramble)

    current_h = x
    current_g = 0
    current_f = x

    limit = current_f
    
    found = False

    iterations = 1

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
                    if correct == child:
                        found = True
                        end = time.time()
                        print("Found solution")
                        print(end - start)
                        print("Itaeration", iterations)
                        return found
                    current_h = ManhattenIDAstar(child)
                    current_g = parent_g + 1
                    current_f = current_g + current_h
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
        print("Not Found")
        return False
