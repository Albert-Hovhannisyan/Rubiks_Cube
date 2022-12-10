from Cube import Cube, perform
from collections import deque 

initial = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
move_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def ManhattenIDAstar(goal):

    if initial == goal:
        return 0

    queue = deque()
    counter = 0
    moves = 0
    sum = 0

    for i in initial:
        moves = 0
        found = False
        queue.append([initial, moves])
        if initial.index(i) == goal.index(i):
            found = True
        while queue:
            if found:
                break 
            curr = queue.popleft()
            if curr[0].index(i) == goal.index(i):
                counter += 1
                sum += curr[1]
                break
            moves += 1
            for k in move_list:
                cube = Cube(curr[0])
                perform(cube, k)
                state = cube.get_state()
                statem = curr[1] + 1
                if state.index(i) == goal.index(i):
                    counter += 1
                    sum += statem
                    found = True
                    break
                queue.append([state, statem])
            if found:
                break
        queue.clear()
    return sum/counter
