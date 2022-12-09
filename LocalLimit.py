from collections import deque
import math
from queue import LifoQueue, PriorityQueue
from Cube import Cube, perform
from Manhatten import Manhatten
import time


correct = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
rotation = ['Y7', 'G2', 'W9', 'R8', 'R5', 'R2', 'R9', 'R6', 'R3', 'Y3', 'B2', 'W1', 'O8', 'O5', 'O2', 'O9', 'O6', 'O3', 'B9', 'Y4', 'G3', 'B6', 'Y5', 'G6', 'B3', 'Y6', 'G9', 'G7', 'G4', 'G1', 'W4', 'W5', 'W6', 'B1', 'B4', 'B7', 'O7', 'O4', 'O1', 'Y8', 'G5', 'W8', 'Y9', 'G8', 'W7', 'R7', 'R4', 'R1', 'Y2', 'B5', 'W2', 'Y1', 'B8', 'W3']
move_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def LocalLimit(scramble):
    if scramble == correct:
        return scramble

    start = time.time()

    node = [[scramble, Manhatten(scramble), -1]]
    count = 0

    while len(node) != 0:
        count += 1
        print(count)
        parent = node.pop()
        if count == 20:
            end = time.time()
            print(end - start)
            return parent[0]
        for i in move_list:
            if math.floor(i/3) != parent[2]:
                tmp = Cube(parent[0])
                perform(tmp, i)
                child = tmp.get_state()
                result = [[child, Manhatten(child), math.floor(i/3)]]
                if child == correct:
                    end = time.time()
                    print(end - start)
                    return True
                if len(node) == 0:
                    node = result
                if node[0][1] > result[0][1]:
                    node = result
        print(node)
    print("Not found")

# b = ['W9', 'R8', 'O1', 'W6', 'R5', 'W4', 'W3', 'B2', 'W1', 'Y9', 'Y8', 'Y1', 'O8', 'O5', 'Y2', 'O9', 'O6', 'R1', 'B1', 'R2', 'R3', 'R4', 'Y5', 'R6', 'O7', 'W2', 'G3', 'R9', 'Y4', 'R7', 'G2', 'W5', 'O4', 'Y7', 'B4', 'B7', 'Y3', 'G4', 'G1', 'B8', 'G5', 'W8', 'B9', 'G6', 'W7', 'O3', 'B6', 'G9', 'O2', 'B5', 'G8', 'B3', 'Y6', 'G7']
# six = ['O9', 'O8', 'Y3', 'G2', 'R5', 'R6', 'Y1', 'B8', 'B3', 'R3', 'B2', 'W1', 'R2', 'O5', 'O2', 'G7', 'O4', 'O7', 'B9', 'Y4', 'G1', 'B6', 'Y5', 'W6', 'W7', 'W8', 'O1', 'B1', 'W4', 'R1', 'B4', 'W5', 'W2', 'G9', 'G6', 'W3', 'G3', 'G8', 'Y9', 'G4', 'G5', 'Y8', 'Y7', 'R8', 'R9', 'R7', 'R4', 'B7', 'Y2', 'B5', 'Y6', 'W9', 'O6', 'O3']
# five = ['O9', 'O8', 'Y3', 'G2', 'R5', 'R6', 'Y7', 'R8', 'R9', 'R3', 'B2', 'W1', 'R2', 'O5', 'O2', 'W9', 'O6', 'O3', 'B9', 'Y4', 'G1', 'B6', 'Y5', 'W6', 'W7', 'W8', 'O1', 'R1', 'W2', 'W3', 'W4', 'W5', 'G6', 'B1', 'B4', 'G9', 'G3', 'G8', 'Y9', 'G4', 'G5', 'Y8', 'G7', 'O4', 'O7', 'R7', 'R4', 'B7', 'Y2', 'B5', 'Y6', 'Y1', 'B8', 'B3']

# a = LocalLimit(five)
# print(a)