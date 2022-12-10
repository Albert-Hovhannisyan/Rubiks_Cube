import math
from Cube import Cube, perform
from ManhattenLocal import ManhattenLocal
import time


correct = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
move_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def LocalSideways(scramble):
    if scramble == correct:
        return scramble

    start = time.time()

    node = [[scramble, ManhattenLocal(scramble), -1]]
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
                result = [[child, ManhattenLocal(child), math.floor(i/3)]]
                if child == correct:
                    end = time.time()
                    print(end - start)
                    print("Found")
                    return True
                if len(node) == 0:
                    node = result
                if node[0][1] > result[0][1]:
                    node = result
        print(node)
    print("Not found")