# move_list = [F,a.F2,a.FP,a.B,a.B2,a.BP,a.L,a.L2,a.LP,a.R,a.R2,a.RP,a.U,a.U2,a.UP,a.D,a.D2,a.DP] 
#move_list[6]() 
move_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
 
from collections import deque

from Cube import Cube, perform 

def h_bfs(goal): 
    correct = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9",  
        "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9",  
        "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9",  
        "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9",  
        "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9",  
        "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"] 
     
    if goal == correct: 
        return goal
     
    levels_dict = {correct:0}
    queue = deque() 
    queue.append(correct) 
     
    visited = [] 
     
    if goal not in visited: 
        while queue: 
            counter = 1 
            node = queue.pop(0) 
            visited.append(node) 
            for i in move_list: 
                levels_dict[counter] = perform(node, i) 
            counter += 1 
    return levels_dict 

trial = ['R7', 'R4', 'R1', 'R8', 'R5', 'R2', 'R9', 'R6', 'R3', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O8', 'O9', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'B9', 'B6', 'B3', 'G7', 'G4', 'G1', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'Y7', 'G2', 'G3', 'Y8', 'G5', 'G6', 'Y9', 'G8', 'G9', 'B1', 'B2', 'W1', 'B4', 'B5', 'W2', 'B7', 'B8', 'W3']             
h_bfs(trial)