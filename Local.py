from collections import deque
from queue import LifoQueue, PriorityQueue
from Cube import Cube, perform
from Manhatten import Manhatten

correct = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
rotation = ['Y7', 'G2', 'W9', 'R8', 'R5', 'R2', 'R9', 'R6', 'R3', 'Y3', 'B2', 'W1', 'O8', 'O5', 'O2', 'O9', 'O6', 'O3', 'B9', 'Y4', 'G3', 'B6', 'Y5', 'G6', 'B3', 'Y6', 'G9', 'G7', 'G4', 'G1', 'W4', 'W5', 'W6', 'B1', 'B4', 'B7', 'O7', 'O4', 'O1', 'Y8', 'G5', 'W8', 'Y9', 'G8', 'W7', 'R7', 'R4', 'R1', 'Y2', 'B5', 'W2', 'Y1', 'B8', 'W3']
move_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

# children = deque() 

def Local(scramble):
    if scramble == correct:
        return scramble

    found = False
    queue = [[scramble, Manhatten(scramble)]]
    count = 0

    while found == False:
        print(count)
        count += 1
        parent = queue.pop()
        for i in move_list:
            tmp = Cube(parent[0])
            perform(tmp, i)
            child = tmp.get_state()
            result = [[child, Manhatten(child)]]
            if child == correct:
                print(result)
                return True
            if  len(queue) == 0:
                queue = result
            if  queue[0][1] > result[0][1]:
                queue = result
        print(queue)

a = Local(rotation)
print(a)