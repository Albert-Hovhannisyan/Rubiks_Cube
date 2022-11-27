import numpy as np

class Cube:
    def __init__(self):
        self.front = np.array([
            ["R1", "R2", "R3"],
            ["R4", "R5", "R6"],
            ["R7", "R8", "R9"]])
        
        self.back = np.array([
            ["O1", "O2", "O3"],
            ["O4", "O5", "O6"],
            ["O7", "O8", "O9"]])

        self.up = np.array([
            ["Y1", "Y2", "Y3"],
            ["Y4", "Y5", "Y6"],
            ["Y7", "Y8", "Y9"]])

        self.down = np.array([
            ["W1", "W2", "W3"],
            ["W4", "W5", "W6"],
            ["W7", "W8", "W9"]])

        self.right = np.array([
            ["G1", "G2", "G3"],
            ["G4", "G5", "G6"],
            ["G7", "G8", "G9"]])

        self.left = np.array([
            ["B1", "B2", "B3"],
            ["B4", "B5", "B6"],
            ["B7", "B8", "B9"]])

    def get_front(self):
        return self.front
      
    def set_front(self, x):
        self.front = x

    def get_back(self):
        return self.back
      
    def set_back(self, x):
        self.back = x

    def get_up(self):
        return self.up
      
    def set_up(self, x):
        self.up = x

    def get_down(self):
        return self.down
      
    def set_down(self, x):
        self.down = x

    def get_right(self):
        return self.right
      
    def set_right(self, x):
        self.right = x

    def get_left(self):
        return self.left
      
    def set_left(self, x):
        self.left = x

    def F(self):
        tmp = rotate(self.get_front(), -1)
        self.set_front(tmp)
        tmp = swapfacesFront(self.get_up(), self.get_left(), self.get_down(), self.get_right(), 1)
        self.set_up(tmp[0])
        self.set_left(tmp[1])
        self.set_down(tmp[2])
        self.set_right(tmp[3])
        print(self.get_front())
        print(self.get_up())
        print(self.get_left())
        print(self.get_down())
        print(self.get_right())

    def F2(self):
        tmp = rotate(self.get_front(), 2)
        self.set_front(tmp)
        tmp = swapfacesFront(self.get_up(), self.get_left(), self.get_down(), self.get_right(), 2)
        self.set_up(tmp[0])
        self.set_left(tmp[1])
        self.set_down(tmp[2])
        self.set_right(tmp[3])
        print(self.get_front())
        print(self.get_up())
        print(self.get_left())
        print(self.get_down())
        print(self.get_right())

    def FP(self):
        tmp = rotate(self.get_front(), 1)
        self.set_front(tmp)
        tmp = swapfacesFront(self.get_up(), self.get_left(), self.get_down(), self.get_right(), 3)
        self.set_up(tmp[0])
        self.set_left(tmp[1])
        self.set_down(tmp[2])
        self.set_right(tmp[3])
        print(self.get_front())
        print(self.get_up())
        print(self.get_left())
        print(self.get_down())
        print(self.get_right())

    def B(self):
        tmp = rotate(self.get_back(), -1)
        self.set_back(tmp)
        tmp = swapfacesBack(self.get_up(), self.get_right(), self.get_down(), self.get_left(), 1)
        self.set_up(tmp[0])
        self.set_right(tmp[1])
        self.set_down(tmp[2])
        self.set_left(tmp[3])
        print(self.get_back())
        print(self.get_up())
        print(self.get_right())
        print(self.get_down())
        print(self.get_left())
    
    def B2(self):
        tmp = rotate(self.get_back(), 2)
        self.set_back(tmp)
        tmp = swapfacesBack(self.get_up(), self.get_right(), self.get_down(), self.get_left(), 2)
        self.set_up(tmp[0])
        self.set_right(tmp[1])
        self.set_down(tmp[2])
        self.set_left(tmp[3])
        print(self.get_back())
        print(self.get_up())
        print(self.get_right())
        print(self.get_down())
        print(self.get_left())

    def BP(self):
        tmp = rotate(self.get_back(), 1)
        self.set_back(tmp)
        tmp = swapfacesBack(self.get_up(), self.get_right(), self.get_down(), self.get_left(), 3)
        self.set_up(tmp[0])
        self.set_right(tmp[1])
        self.set_down(tmp[2])
        self.set_left(tmp[3])
        print(self.get_back())
        print(self.get_up())
        print(self.get_right())
        print(self.get_down())
        print(self.get_left())

    def L(self):
        tmp = rotate(self.get_left(), -1)
        self.set_left(tmp)
        tmp = swapfacesLeft(self.get_up(), self.get_back(), self.get_down(), self.get_front(), 1)
        self.set_up(tmp[0])
        self.set_back(tmp[1])
        self.set_down(tmp[2])
        self.set_front(tmp[3])
        print(self.get_left())
        print(self.get_up())
        print(self.get_back())
        print(self.get_down())
        print(self.get_front())
    
    def L2(self):
        tmp = rotate(self.get_left(), 2)
        self.set_left(tmp)
        tmp = swapfacesLeft(self.get_up(), self.get_back(), self.get_down(), self.get_front(), 2)
        self.set_up(tmp[0])
        self.set_back(tmp[1])
        self.set_down(tmp[2])
        self.set_front(tmp[3])
        print(self.get_left())
        print(self.get_up())
        print(self.get_back())
        print(self.get_down())
        print(self.get_front())
    
    def LP(self):
        tmp = rotate(self.get_left(), 1)
        self.set_left(tmp)
        tmp = swapfacesLeft(self.get_up(), self.get_back(), self.get_down(), self.get_front(), 3)
        self.set_up(tmp[0])
        self.set_back(tmp[1])
        self.set_down(tmp[2])
        self.set_front(tmp[3])
        print(self.get_left())
        print(self.get_up())
        print(self.get_back())
        print(self.get_down())
        print(self.get_front())

    def R(self):
        tmp = rotate(self.get_right(), -1)
        self.set_right(tmp)
        tmp = swapfacesRight(self.get_up(), self.get_front(), self.get_down(), self.get_back(), 1)
        self.set_up(tmp[0])
        self.set_front(tmp[1])
        self.set_down(tmp[2])
        self.set_back(tmp[3])
        print(self.get_right())
        print(self.get_up())
        print(self.get_front())
        print(self.get_down())
        print(self.get_back())

    def R2(self):
        tmp = rotate(self.get_right(), 2)
        self.set_right(tmp)
        tmp = swapfacesRight(self.get_up(), self.get_front(), self.get_down(), self.get_back(), 2)
        self.set_up(tmp[0])
        self.set_front(tmp[1])
        self.set_down(tmp[2])
        self.set_back(tmp[3])
        print(self.get_right())
        print(self.get_up())
        print(self.get_front())
        print(self.get_down())
        print(self.get_back())

    def RP(self):
        tmp = rotate(self.get_right(), 1)
        self.set_right(tmp)
        tmp = swapfacesRight(self.get_up(), self.get_front(), self.get_down(), self.get_back(), 3)
        self.set_up(tmp[0])
        self.set_front(tmp[1])
        self.set_down(tmp[2])
        self.set_back(tmp[3])
        print(self.get_right())
        print(self.get_up())
        print(self.get_front())
        print(self.get_down())
        print(self.get_back())    

    def U(self):
        tmp = rotate(self.get_up(), -1)
        self.set_up(tmp)
        tmp = swapfacesUp(self.get_front(), self.get_right(), self.get_back(), self.get_left(), 1)
        self.set_front(tmp[0])
        self.set_right(tmp[1])
        self.set_back(tmp[2])
        self.set_left(tmp[3])
        print(self.get_up())
        print(self.get_front())
        print(self.get_right())
        print(self.get_back())
        print(self.get_left())

    def U2(self):
        tmp = rotate(self.get_up(), 2)
        self.set_up(tmp)
        tmp = swapfacesUp(self.get_front(), self.get_right(), self.get_back(), self.get_left(), 2)
        self.set_front(tmp[0])
        self.set_right(tmp[1])
        self.set_back(tmp[2])
        self.set_left(tmp[3])
        print(self.get_up())
        print(self.get_front())
        print(self.get_right())
        print(self.get_back())
        print(self.get_left())

    def UP(self):
        tmp = rotate(self.get_up(), 1)
        self.set_up(tmp)
        tmp = swapfacesUp(self.get_front(), self.get_right(), self.get_back(), self.get_left(), 3)
        self.set_front(tmp[0])
        self.set_right(tmp[1])
        self.set_back(tmp[2])
        self.set_left(tmp[3])
        print(self.get_up())
        print(self.get_front())
        print(self.get_right())
        print(self.get_back())
        print(self.get_left())

    def D(self):
        tmp = rotate(self.get_down(), -1)
        self.set_down(tmp)
        tmp = swapfacesDown(self.get_front(), self.get_left(), self.get_back(), self.get_right(), 1)
        self.set_front(tmp[0])
        self.set_left(tmp[1])
        self.set_back(tmp[2])
        self.set_right(tmp[3])
        print(self.get_down())
        print(self.get_front())
        print(self.get_left())
        print(self.get_back())
        print(self.get_right())

    def D2(self):
        tmp = rotate(self.get_down(), 2)
        self.set_down(tmp)
        tmp = swapfacesDown(self.get_front(), self.get_left(), self.get_back(), self.get_right(), 2)
        self.set_front(tmp[0])
        self.set_left(tmp[1])
        self.set_back(tmp[2])
        self.set_right(tmp[3])
        print(self.get_down())
        print(self.get_front())
        print(self.get_left())
        print(self.get_back())
        print(self.get_right())

    def DP(self):
        tmp = rotate(self.get_down(), 1)
        self.set_down(tmp)
        tmp = swapfacesDown(self.get_front(), self.get_left(), self.get_back(), self.get_right(), 3)
        self.set_front(tmp[0])
        self.set_left(tmp[1])
        self.set_back(tmp[2])
        self.set_right(tmp[3])
        print(self.get_down())
        print(self.get_front())
        print(self.get_left())
        print(self.get_back())
        print(self.get_right())

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

