from collections import deque
from Cube import Cube, perform 
import time

move_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
 
initial = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
trial = ['Y7', 'G2', 'O9', 'R8', 'R5', 'O8', 'R9', 'R6', 'Y3', 'R3', 'B2', 'W1', 'R2', 'O5', 'O2', 'W9', 'O6', 'O3', 'B9', 'Y4', 'G1', 'B6', 'Y5', 'W6', 'B3', 'Y6', 'B7', 'G7', 'G4', 'G3', 'W4', 'W5', 'G6', 'B1', 'B4', 'G9', 'W7', 'G8', 'Y9', 'W8', 'G5', 'Y8', 'O1', 'O4', 'O7', 'R7', 'R4', 'R1', 'Y2', 'B5', 'W2', 'Y1', 'B8', 'W3']
one = ['W1', 'R2', 'R3', 'W4', 'R5', 'R6', 'W7', 'R8', 'R9', 'O1', 'O2', 'Y7', 'O4', 'O5', 'Y4', 'O7', 'O8', 'Y1', 'R1', 'Y2', 'Y3', 'R4', 'Y5', 'Y6', 'R7', 'Y8', 'Y9', 'O9', 'W2', 'W3', 'O6', 'W5', 'W6', 'O3', 'W8', 'W9', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'B3', 'B6', 'B9', 'B2', 'B5', 'B8', 'B1', 'B4', 'B7']
two = ['R7', 'R4', 'R1', 'R8', 'R5', 'R2', 'R9', 'R6', 'R3', 'O7', 'O4', 'O1', 'O8', 'O5', 'O2', 'O9', 'O6', 'O3', 'G3', 'G6', 'G9', 'Y4', 'Y5', 'Y6', 'B9', 'B6', 'B3', 'G7', 'G4', 'G1', 'W4', 'W5', 'W6', 'B1', 'B4', 'B7', 'Y7', 'G2', 'W9', 'Y8', 'G5', 'W8', 'Y9', 'G8', 'W7', 'Y3', 'B2', 'W1', 'Y2', 'B5', 'W2', 'Y1', 'B8', 'W3']
tree = ['Y7', 'G2', 'W9', 'R8', 'R5', 'R2', 'R9', 'R6', 'R3', 'Y3', 'B2', 'W1', 'O8', 'O5', 'O2', 'O9', 'O6', 'O3', 'B9', 'Y4', 'G3', 'B6', 'Y5', 'G6', 'B3', 'Y6', 'G9', 'G7', 'G4', 'G1', 'W4', 'W5', 'W6', 'B1', 'B4', 'B7', 'O7', 'O4', 'O1', 'Y8', 'G5', 'W8', 'Y9', 'G8', 'W7', 'R7', 'R4', 'R1', 'Y2', 'B5', 'W2', 'Y1', 'B8', 'W3']
five = ['O9', 'O8', 'Y3', 'G2', 'R5', 'R6', 'Y7', 'R8', 'R9', 'R3', 'B2', 'W1', 'R2', 'O5', 'O2', 'W9', 'O6', 'O3', 'B9', 'Y4', 'G1', 'B6', 'Y5', 'W6', 'W7', 'W8', 'O1', 'R1', 'W2', 'W3', 'W4', 'W5', 'G6', 'B1', 'B4', 'G9', 'G3', 'G8', 'Y9', 'G4', 'G5', 'Y8', 'G7', 'O4', 'O7', 'R7', 'R4', 'B7', 'Y2', 'B5', 'Y6', 'Y1', 'B8', 'B3']
six = ['O9', 'O8', 'Y3', 'G2', 'R5', 'R6', 'Y1', 'B8', 'B3', 'R3', 'B2', 'W1', 'R2', 'O5', 'O2', 'G7', 'O4', 'O7', 'B9', 'Y4', 'G1', 'B6', 'Y5', 'W6', 'W7', 'W8', 'O1', 'B1', 'W4', 'R1', 'B4', 'W5', 'W2', 'G9', 'G6', 'W3', 'G3', 'G8', 'Y9', 'G4', 'G5', 'Y8', 'Y7', 'R8', 'R9', 'R7', 'R4', 'B7', 'Y2', 'B5', 'Y6', 'W9', 'O6', 'O3']
only = ['R7', 'R4', 'R1', 'R8', 'R5', 'R2', 'R9', 'R6', 'R3', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'B9', 'B6', 'B3', 'G7', 'G4', 'G1', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'Y7', 'G2', 'G3', 'Y8', 'G5', 'G6', 'Y9', 'G8', 'G9', 'B1', 'B2', 'W1', 'B4', 'B5', 'W2', 'B7', 'B8', 'W3']

def bfs(goal): 
    start = time.time()
    if goal == initial: 
        return 0
     
    # levels_dict = {initial:0}
     
    queue = deque() 
    visited = []
    count = 0
     
    queue.append([goal, ["Start"]])

    if initial not in visited: 
        while queue: 
            node = queue.popleft() 
            visited.append(node) 
            for i in move_list: 
                cube = Cube(node[0])
                perform(cube, i)
                state = cube.get_state()
                moves = node[1].copy()
                moves.append(i)
                if initial == state:
                    print(count)
                    end = time.time()
                    print(end - start)
                    return moves
                queue.append([state, moves])
                count += 1
    return count 

result = bfs(only)
print(result)