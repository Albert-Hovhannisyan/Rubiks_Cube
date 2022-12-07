import numpy as np

class Cube:
    def __init__(self, state):

        self.state = state.copy()

        self.front = np.array([
            [state[0], state[1], state[2]],
            [state[3], state[4], state[5]],
            [state[6], state[7], state[8]]])
        
        self.back = np.array([
            [state[9], state[10], state[11]],
            [state[12], state[13], state[14]],
            [state[15], state[16], state[17]]])

        self.up = np.array([
            [state[18], state[19], state[20]],
            [state[21], state[22], state[23]],
            [state[24], state[25], state[26]]])

        self.down = np.array([
            [state[27], state[28], state[29]],
            [state[30], state[31], state[32]],
            [state[33], state[34], state[35]]])

        self.right = np.array([
            [state[36], state[37], state[38]],
            [state[39], state[40], state[41]],
            [state[42], state[43], state[44]]])

        self.left = np.array([
            [state[45], state[46], state[47]],
            [state[48], state[49], state[50]],
            [state[51], state[52], state[53]]])

    def get_front(self):
        return self.front
      
    def set_front(self, x):
        self.front = x
        count = 0
        for i in range(3):
            for j in range(3):
                self.state[count] = self.front[i][j]
                count += 1

    def get_back(self):
        return self.back
      
    def set_back(self, x):
        self.back = x
        count = 9
        for i in range(3):
            for j in range(3):
                self.state[count] = self.back[i][j]
                count += 1

    def get_up(self):
        return self.up
      
    def set_up(self, x):
        self.up = x
        count = 18
        for i in range(3):
            for j in range(3):
                self.state[count] = self.up[i][j]
                count += 1

    def get_down(self):
        return self.down
      
    def set_down(self, x):
        self.down = x
        count = 27
        for i in range(3):
            for j in range(3):
                self.state[count] = self.down[i][j]
                count += 1

    def get_right(self):
        return self.right
      
    def set_right(self, x):
        self.right = x
        count = 36
        for i in range(3):
            for j in range(3):
                self.state[count] = self.right[i][j]
                count += 1

    def get_left(self):
        return self.left
      
    def set_left(self, x):
        self.left = x
        count = 45
        for i in range(3):
            for j in range(3):
                self.state[count] = self.left[i][j]
                count += 1

    def get_state(self):
        return self.state
    
    def set_state(self, x):
        self.state = x

    def print_cube(self):
        print("Front")
        print(self.front)
        print("Back")
        print(self.back)
        print("Up")
        print(self.up)
        print("Down")
        print(self.down)
        print("Right")
        print(self.right)
        print("Left")
        print(self.left)

    def F(self):
        tmp = rotate(self.front, -1)
        self.set_front(tmp)
        tmp = swapfacesFront(self.up, self.left, self.down, self.right, 1)
        self.set_up(tmp[0])
        self.set_left(tmp[1])
        self.set_down(tmp[2])
        self.set_right(tmp[3])

    def F2(self):
        tmp = rotate(self.front, 2)
        self.set_front(tmp)
        tmp = swapfacesFront(self.up, self.left, self.down, self.right, 2)
        self.set_up(tmp[0])
        self.set_left(tmp[1])
        self.set_down(tmp[2])
        self.set_right(tmp[3])

    def FP(self):
        tmp = rotate(self.front, 1)
        self.set_front(tmp)
        tmp = swapfacesFront(self.up, self.left, self.down, self.right, 3)
        self.set_up(tmp[0])
        self.set_left(tmp[1])
        self.set_down(tmp[2])
        self.set_right(tmp[3])

    def B(self):
        tmp = rotate(self.back, -1)
        self.set_back(tmp)
        tmp = swapfacesBack(self.up, self.right, self.down, self.left, 1)
        self.set_up(tmp[0])
        self.set_right(tmp[1])
        self.set_down(tmp[2])
        self.set_left(tmp[3])
    
    def B2(self):
        tmp = rotate(self.back, 2)
        self.set_back(tmp)
        tmp = swapfacesBack(self.up, self.right, self.down, self.left, 2)
        self.set_up(tmp[0])
        self.set_right(tmp[1])
        self.set_down(tmp[2])
        self.set_left(tmp[3])

    def BP(self):
        tmp = rotate(self.back, 1)
        self.set_back(tmp)
        tmp = swapfacesBack(self.up, self.right, self.down, self.left, 3)
        self.set_up(tmp[0])
        self.set_right(tmp[1])
        self.set_down(tmp[2])
        self.set_left(tmp[3])

    def L(self):
        tmp = rotate(self.left, -1)
        self.set_left(tmp)
        tmp = swapfacesLeft(self.up, self.back, self.down, self.front, 1)
        self.set_up(tmp[0])
        self.set_back(tmp[1])
        self.set_down(tmp[2])
        self.set_front(tmp[3])
    
    def L2(self):
        tmp = rotate(self.left, 2)
        self.set_left(tmp)
        tmp = swapfacesLeft(self.up, self.back, self.down, self.front, 2)
        self.set_up(tmp[0])
        self.set_back(tmp[1])
        self.set_down(tmp[2])
        self.set_front(tmp[3])
    
    def LP(self):
        tmp = rotate(self.left, 1)
        self.set_left(tmp)
        tmp = swapfacesLeft(self.up, self.back, self.down, self.front, 3)
        self.set_up(tmp[0])
        self.set_back(tmp[1])
        self.set_down(tmp[2])
        self.set_front(tmp[3])

    def R(self):
        tmp = rotate(self.right, -1)
        self.set_right(tmp)
        tmp = swapfacesRight(self.up, self.front, self.down, self.back, 1)
        self.set_up(tmp[0])
        self.set_front(tmp[1])
        self.set_down(tmp[2])
        self.set_back(tmp[3])

    def R2(self):
        tmp = rotate(self.right, 2)
        self.set_right(tmp)
        tmp = swapfacesRight(self.up, self.front, self.down, self.back, 2)
        self.set_up(tmp[0])
        self.set_front(tmp[1])
        self.set_down(tmp[2])
        self.set_back(tmp[3])

    def RP(self):
        tmp = rotate(self.right, 1)
        self.set_right(tmp)
        tmp = swapfacesRight(self.up, self.front, self.down, self.back, 3)
        self.set_up(tmp[0])
        self.set_front(tmp[1])
        self.set_down(tmp[2])
        self.set_back(tmp[3])    

    def U(self):
        tmp = rotate(self.up, -1)
        self.set_up(tmp)
        tmp = swapfacesUp(self.front, self.right, self.back, self.left, 1)
        self.set_front(tmp[0])
        self.set_right(tmp[1])
        self.set_back(tmp[2])
        self.set_left(tmp[3])

    def U2(self):
        tmp = rotate(self.up, 2)
        self.set_up(tmp)
        tmp = swapfacesUp(self.front, self.right, self.back, self.left, 2)
        self.set_front(tmp[0])
        self.set_right(tmp[1])
        self.set_back(tmp[2])
        self.set_left(tmp[3])

    def UP(self):
        tmp = rotate(self.up, 1)
        self.set_up(tmp)
        tmp = swapfacesUp(self.front, self.right, self.back, self.left, 3)
        self.set_front(tmp[0])
        self.set_right(tmp[1])
        self.set_back(tmp[2])
        self.set_left(tmp[3])

    def D(self):
        tmp = rotate(self.down, -1)
        self.set_down(tmp)
        tmp = swapfacesDown(self.front, self.left, self.back, self.right, 1)
        self.set_front(tmp[0])
        self.set_left(tmp[1])
        self.set_back(tmp[2])
        self.set_right(tmp[3])

    def D2(self):
        tmp = rotate(self.down, 2)
        self.set_down(tmp)
        tmp = swapfacesDown(self.front, self.left, self.back, self.right, 2)
        self.set_front(tmp[0])
        self.set_left(tmp[1])
        self.set_back(tmp[2])
        self.set_right(tmp[3])

    def DP(self):
        tmp = rotate(self.down, 1)
        self.set_down(tmp)
        tmp = swapfacesDown(self.front, self.left, self.back, self.right, 3)
        self.set_front(tmp[0])
        self.set_left(tmp[1])
        self.set_back(tmp[2])
        self.set_right(tmp[3])

def rotate(face, x):
    return np.rot90(face, x)

def swapfacesFront(up, left, down, right, n):

    for j in range(n):
        tmp = [up[2][0], up[2][1], up[2][2]]

        up[2][0] = left[2][2]
        up[2][1] = left[1][2]
        up[2][2] = left[0][2]

        left[0][2] = down[0][0]
        left[1][2] = down[0][1]
        left[2][2] = down[0][2]

        down[0][0] = right[2][0]
        down[0][1] = right[1][0]
        down[0][2] = right[0][0]

        right[0][0] = tmp[0]
        right[1][0] = tmp[1]
        right[2][0] = tmp[2]

    return [up, left, down, right]

def swapfacesBack(up, right, down, left, n):

    for j in range(n):
        tmp = [up[0][0], up[0][1], up[0][2]]

        up[0][0] = right[0][2]
        up[0][1] = right[1][2]
        up[0][2] = right[2][2]

        right[0][2] = down[2][2]
        right[1][2] = down[2][1]
        right[2][2] = down[2][0]

        down[2][0] = left[0][0]
        down[2][1] = left[1][0]
        down[2][2] = left[2][0]

        left[0][0] = tmp[2]
        left[1][0] = tmp[1]
        left[2][0] = tmp[0]

    return [up, right, down, left]

def swapfacesUp(front, right, back, left, n):
    for j in range(n):
        tmp = [front[0][0], front[0][1], front[0][2]]

        front[0][0] = right[0][0]
        front[0][1] = right[0][1]
        front[0][2] = right[0][2]

        right[0][0] = back[0][0]
        right[0][1] = back[0][1]
        right[0][2] = back[0][2]

        back[0][0] = left[0][0]
        back[0][1] = left[0][1]
        back[0][2] = left[0][2]

        left[0][0] = tmp[0]
        left[0][1] = tmp[1]
        left[0][2] = tmp[2]

    return [front, right, back, left]

def swapfacesDown(front, left, back, right, n):
    for j in range(n):
        tmp = [front[2][0], front[2][1], front[2][2]]

        front[2][0] = left[2][0]
        front[2][1] = left[2][1]
        front[2][2] = left[2][2]

        left[2][0] = back[2][0]
        left[2][1] = back[2][1]
        left[2][2] = back[2][2]

        back[2][0] = right[2][0]
        back[2][1] = right[2][1]
        back[2][2] = right[2][2]

        right[2][0] = tmp[0]
        right[2][1] = tmp[1]
        right[2][2] = tmp[2]

    return [front, left, back, right]

def swapfacesLeft(up, back, down, front, n):
    for j in range(n):
        tmp = [up[0][0], up[1][0], up[2][0]]

        up[0][0] = back[2][2]
        up[1][0] = back[1][2]
        up[2][0] = back[0][2]

        back[0][2] = down[2][0]
        back[1][2] = down[1][0]
        back[2][2] = down[0][0]

        down[0][0] = front[0][0]
        down[1][0] = front[1][0]
        down[2][0] = front[2][0]

        front[0][0] = tmp[0]
        front[1][0] = tmp[1]
        front[2][0] = tmp[2]

    return [up, back, down, front]

def swapfacesRight(up, front, down, back, n):
    for j in range(n):
        tmp = [up[0][2], up[1][2], up[2][2]]

        up[0][2] = front[0][2]
        up[1][2] = front[1][2]
        up[2][2] = front[2][2]

        front[0][2] = down[0][2]
        front[1][2] = down[1][2]
        front[2][2] = down[2][2]

        down[0][2] = back[2][0]
        down[1][2] = back[1][0]
        down[2][2] = back[0][0]

        back[0][0] = tmp[2]
        back[1][0] = tmp[1]
        back[2][0] = tmp[0]

    return [up, front, down, back]

goal = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "O1", "O2", "O3", "O4", "O5", "O6", "O7", "O8", "O9", "Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "W1", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9"]
trial = ['O9', 'O8', 'O7', 'G2', 'R5', 'R8', 'Y7', 'B8', 'Y9', 'R9', 'O4', 'B1', 'R6', 'O5', 'B2', 'W1', 'O2', 'O1', 'O3', 'G6', 'W3', 'Y8', 'Y5', 'W6', 'W7', 'W8', 'W9', 'R1', 'W4', 'R3', 'B4', 'W5', 'B6', 'Y3', 'Y2', 'B9', 'G9', 'G8', 'G7', 'W2', 'G5', 'G4', 'G1', 'R4', 'R7', 'Y1', 'R2', 'B7', 'Y4', 'B5', 'Y6', 'G3', 'O6', 'B3']
cube = Cube(goal)

cube.UP()
# cube.R()
# cube.B()
# cube.LP()
# cube.F2()
# cube.B()
# cube.U()
# cube.R2()
# cube.FP()
# cube.D()
# print(cube.get_state())
# cube.print_cube()

# print(goal.index("R2"))

# Cube(goal).get_state()

function_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

def perform(obj, i):
    match i:
        case 0:
            obj.F()
        case 1:
            obj.F2()
        case 2:
            obj.FP()
        case 3:
            obj.B()
        case 4:
            obj.B2()
        case 5:
            obj.BP()
        case 6:
            obj.U()
        case 7:
            obj.U2()
        case 8:
            obj.UP()
        case 9:
            obj.D()
        case 10:
            obj.D2()
        case 11:
            obj.DP()
        case 12:
            obj.R()
        case 13:
            obj.R2()
        case 14:
            obj.RP()
        case 15:
            obj.L()
        case 16:
            obj.L2()
        case 17:
            obj.LP()
            
# perform(cube, 0)

# cube.F()
# # cube.FP()

# if(goal == cube.get_state()):
#     print(True)
# else:
#     print(False)

# print(goal)
# print(cube.get_state())


# cube.F2()
# cube.B2()
# cube.B2()
# cube.L2()
# cube.L2()
# cube.U2()
# cube.U2()
# cube.R2()
# cube.R2()
# cube.D2()
# cube.D2()

# cube.F()
# cube.B()
# cube.L()
# cube.U()
# cube.R()
# cube.D()
# cube.DP()
# cube.RP()
# cube.UP()
# cube.LP()
# cube.BP()
# cube.FP()

# print(cube.get_state())
# cube.print_cube()