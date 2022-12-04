from Cube import Cube

initial = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
trial = ['O9', 'O8', 'O7', 'G2', 'R5', 'R8', 'G1', 'R4', 'R7', 'R9', 'O4', 'B1', 'R6', 'O5', 'B2', 'G3', 'O6', 'B3', 'O3', 'G6', 'W3', 'Y8', 'Y5', 'W6', 'W7', 'W8', 'W9', 'R3', 'B6', 'B9', 'W4', 'W5', 'Y2', 'R1', 'B4', 'Y3', 'G9', 'G8', 'G7', 'W2', 'G5', 'G4', 'W1', 'O2', 'O1', 'Y1', 'R2', 'B7', 'Y4', 'B5', 'Y6', 'Y7', 'B8', 'Y9']

def Manhatten(goal):
    if initial == goal:
        return 0
    
    sum = 0
    length = len(initial)

    for i in goal:
        if initial.index(i) > goal.index(i):
            tmp = min(initial.index(i) - goal.index(i), length - initial.index(i) + goal.index(i))
            sum += tmp
        else:
            tmp = min(goal.index(i) - initial.index(i), length - goal.index(i) + initial.index(i))
            sum += tmp 
    return sum
        
# result = Manhatten(trial)
# print(result)