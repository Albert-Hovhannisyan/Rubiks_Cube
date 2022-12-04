from Cube import Cube, perform
from collections import deque 

initial = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
trial = ['R7', 'R4', 'R1', 'R8', 'R5', 'R2', 'R9', 'R6', 'R3', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'B9', 'B6', 'B3', 'G7', 'G4', 'G1', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'Y7', 'G2', 'G3', 'Y8', 'G5', 'G6', 'Y9', 'G8', 'G9', 'B1', 'B2', 'W1', 'B4', 'B5', 'W2', 'B7', 'B8', 'W3']
second = ['R7', 'R4', 'G1', 'R8', 'R5', 'W6', 'R9', 'R6', 'W9', 'B3', 'O2', 'O3', 'Y6', 'O5', 'O6', 'Y3', 'O8', 'O9', 'Y1', 'Y2', 'R1', 'Y4', 'Y5', 'R2', 'B9', 'B6', 'R3', 'G7', 'G4', 'O7', 'W4', 'W5', 'O4', 'W7', 'W8', 'O1', 'Y9', 'Y8', 'Y7', 'G8', 'G5', 'G2', 'G9', 'G6', 'G3', 'B1', 'B2', 'W1', 'B4', 'B5', 'W2', 'B7', 'B8', 'W3']
test = ['R9', 'R8', 'R7', 'R6', 'R5', 'R4', 'R3', 'R2', 'R1', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'W3', 'W2', 'W1', 'Y9', 'Y8', 'Y7', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'B9', 'G2', 'G3', 'B6', 'G5', 'G6', 'B3', 'G8', 'G9', 'B1', 'B2', 'G7', 'B4', 'B5', 'G4', 'B7', 'B8', 'G1']
last = ['Y1', 'R2', 'R3', 'Y4', 'R5', 'R6', 'Y7', 'R8', 'R9', 'O1', 'O2', 'W7', 'O4', 'O5', 'W4', 'O7', 'O8', 'W1', 'O9', 'Y2', 'Y3', 'O6', 'Y5', 'Y6', 'O3', 'Y8', 'Y9', 'R1', 'W2', 'W3', 'R4', 'W5', 'W6', 'R7', 'W8', 'W9', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'B7', 'B4', 'B1', 'B8', 'B5', 'B2', 'B9', 'B6', 'B3']
tree = ['Y7', 'G2', 'W9', 'R8', 'R5', 'R2', 'R9', 'R6', 'R3', 'Y3', 'B2', 'W1', 'O8', 'O5', 'O2', 'O9', 'O6', 'O3', 'B9', 'Y4', 'G3', 'B6', 'Y5', 'G6', 'B3', 'Y6', 'G9', 'G7', 'G4', 'G1', 'W4', 'W5', 'W6', 'B1', 'B4', 'B7', 'O7', 'O4', 'O1', 'Y8', 'G5', 'W8', 'Y9', 'G8', 'W7', 'R7', 'R4', 'R1', 'Y2', 'B5', 'W2', 'Y1', 'B8', 'W3']
orange = ['G7', 'G4', 'G1', 'R4', 'R5', 'W6', 'B7', 'B8', 'B9', 'B1', 'B2', 'B3', 'Y6', 'O5', 'O6', 'G9', 'G6', 'G3', 'Y7', 'Y4', 'Y1', 'Y8', 'Y5', 'Y2', 'R9', 'R6', 'R3', 'W7', 'W4', 'W1', 'W8', 'W5', 'W2', 'O1', 'O4', 'O7', 'Y9', 'O2', 'O3', 'G8', 'G5', 'G2', 'R7', 'R8', 'W9', 'R1', 'R2', 'W3', 'B4', 'B5', 'B6', 'Y3', 'O8', 'O9']
move_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def rbfs(goal):

    if initial == goal:
        return 0

    queue = deque()
    visited = []
    moves = 0
    sum = 0

    for i in initial:
        queue.append(initial)
        found = False
        moves = 0
        if initial.index(i) == goal.index(i):
            found = True
        while queue:
            if found:
                break 
            curr = queue.popleft()
            if curr.index(i) == goal.index(i):
                sum += moves
                print(i)
                print(moves)
                break
            moves += 1
            for k in move_list:
                cube = Cube(curr)
                perform(cube, k)
                state = cube.get_state()
                if state.index(i) == goal.index(i):
                    sum += moves
                    print(i)
                    print(moves)
                    found = True
                    break
                queue.append(state)
            if found:
                break
        queue.clear()
    return sum

# result = rbfs(orange)
# print(result)