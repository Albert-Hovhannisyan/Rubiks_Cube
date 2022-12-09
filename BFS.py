from collections import deque
from Cube import Cube, perform 
import time

move_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
 
initial = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]

def bfs(goal): 
    start = time.time()
    if goal == initial: 
        return 0
          
    queue = deque() 
    visited = []
    count = 0
     
    queue.append([goal, ["Start"]])

    if initial == goal:
        return 0

    while queue: 
        node = queue.popleft()
        if node[0] not in visited: 
            visited.append(node[0]) 
            for i in move_list: 
                cube = Cube(node[0])
                perform(cube, i)
                state = cube.get_state()
                if state not in visited:
                    moves = node[1].copy()
                    moves.append(i)
                    queue.append([state, moves])
                if initial == state:
                    print(count)
                    end = time.time()
                    print(end - start)
                    return moves
                count += 1
    return count 

